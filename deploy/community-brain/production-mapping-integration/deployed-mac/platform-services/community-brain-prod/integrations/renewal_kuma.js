const jwt = require('jsonwebtoken');
const fs = require('fs');
const sqlite3 = require('@louislam/sqlite3').verbose();
const {io} = require('socket.io-client');
const {shake256,SHAKE256_LENGTH} = require('/app/server/util-server');
const input=JSON.parse(fs.readFileSync(0,'utf8'));
const db=new sqlite3.Database('/app/data/kuma.db');
const get=(sql,params=[])=>new Promise((resolve,reject)=>db.get(sql,params,(e,r)=>e?reject(e):resolve(r)));
const ack=(s,e,...args)=>new Promise((resolve,reject)=>s.timeout(15000).emit(e,...args,(err,r)=>err||!r?.ok?reject(new Error('Kuma acknowledgment failed '+e+(err?' timeout':' rejected'))):resolve(r)));
async function main(){
 const setting=await get('SELECT value FROM setting WHERE key=?',['jwtSecret']);
 const user=await get('SELECT username,password FROM user WHERE active=1 ORDER BY id LIMIT 1');
 const auth=jwt.sign({username:user.username,h:shake256(user.password,SHAKE256_LENGTH)},setting.value,{expiresIn:180});
 const socket=io('http://127.0.0.1:3001',{transports:['websocket'],reconnection:false,timeout:15000,autoConnect:false});
 // Kuma awaits sendInfo before registering login handlers. Transport connect
 // alone is too early; wait for the application readiness event.
 await new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(new Error('Kuma readiness timeout')),15000);socket.once('info',()=>{clearTimeout(timer);resolve();});socket.once('connect_error',reject);socket.connect();});
 await ack(socket,'loginByToken',auth);
 const pending=new Promise(resolve=>socket.once('monitorList',resolve));await ack(socket,'getMonitorList');const list=await pending;
 const old=list[31];if(!old||old.name!=='community-brain-production-retrieval'||!old.active)throw new Error('Unexpected monitor');
 const headers=JSON.parse(old.headers);if(!['Bearer '+input.old,'Bearer '+input.token].includes(headers.Authorization))throw new Error('Monitor credential drift');
 if(!/^[a-f0-9-]{36}$/.test(input.cycle))throw new Error('Invalid cycle');
 const backup='/app/data/cbm-renewal-'+input.cycle+'.before.json';if(!fs.existsSync(backup))fs.writeFileSync(backup,JSON.stringify(old),{flag:'wx',mode:0o600});
 headers.Authorization='Bearer '+input.token;
 await ack(socket,'editMonitor',{...old,headers:JSON.stringify(headers)});
 const row=await get('SELECT headers,active,url,method FROM monitor WHERE id=31');
 if(JSON.parse(row.headers).Authorization!=='Bearer '+input.token||row.active!==1||row.url!==old.url||row.method!==old.method)throw new Error('Monitor verification failed');
 socket.close();db.close();console.log(JSON.stringify({monitor_id:31,credential_updated:true,active:true,other_settings_preserved:true,private_backup:backup}));
}
main().catch((e)=>{db.close();console.error(e.message.startsWith('Kuma acknowledgment failed')?e.message:'Kuma rotation failed; private output suppressed');process.exit(1);});
