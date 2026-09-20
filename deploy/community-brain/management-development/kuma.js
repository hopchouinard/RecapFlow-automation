// Actual isolated Kuma Socket.IO adapter. No production IDs or database inputs.
const fs=require('fs'), jwt=require('jsonwebtoken');
const sqlite3=require('@louislam/sqlite3').verbose();
const {io}=require('socket.io-client');
const {shake256,SHAKE256_LENGTH}=require('/app/server/util-server');
const input=JSON.parse(fs.readFileSync(0,'utf8'));
const db=new sqlite3.Database('/app/data/kuma.db',sqlite3.OPEN_READONLY);
const get=(q,p=[])=>new Promise((yes,no)=>db.get(q,p,(e,r)=>e?no(e):yes(r)));
const ack=(s,e,...a)=>new Promise((yes,no)=>s.timeout(15000).emit(e,...a,(err,r)=>err||!r?.ok?no(new Error('Kuma acknowledgment failed '+e)):yes(r)));
async function main(){
 const socket=io('http://127.0.0.1:3001',{transports:['websocket'],reconnection:false,timeout:15000,autoConnect:false});
 await new Promise((yes,no)=>{const timer=setTimeout(()=>no(new Error('Kuma readiness timeout')),15000);socket.once('info',()=>{clearTimeout(timer);yes()});socket.once('connect_error',no);socket.connect()});
 let user=await get('SELECT username,password FROM user WHERE active=1 ORDER BY id LIMIT 1');
 if(input.mode==='setup'){
  if(user)throw new Error('Existing development user; reconcile setup');
  await ack(socket,'setup',input.username,input.password);
  user=await get('SELECT username,password FROM user WHERE active=1 ORDER BY id LIMIT 1');
 }
 const secret=await get('SELECT value FROM setting WHERE key=?',['jwtSecret']);
 const token=jwt.sign({username:user.username,h:shake256(user.password,SHAKE256_LENGTH)},secret.value,{expiresIn:180});
 await ack(socket,'loginByToken',token);
 const pending=new Promise(yes=>socket.once('monitorList',yes));await ack(socket,'getMonitorList');
 const list=await pending;let monitor=Object.values(list).find(x=>x.name==='cbm-request027-retrieval');
 if(input.mode==='setup'){
  if(monitor)throw new Error('Existing monitor');
  const value={type:'http',name:'cbm-request027-retrieval',url:'http://api:8090/retrieval/query',method:'POST',body:JSON.stringify({question:'synthetic',top_k:1}),headers:JSON.stringify({'Authorization':'Bearer '+input.token,'Content-Type':'application/json'}),parent:null,interval:20,retryInterval:20,maxretries:0,resendInterval:0,upsideDown:false,expiryNotification:false,ignoreTls:false,maxredirects:0,accepted_statuscodes:['200'],conditions:[],kafkaProducerBrokers:[],kafkaProducerSaslOptions:{},rabbitmqNodes:[],notificationIDList:{}};
  const id=(await ack(socket,'add',value)).monitorID;monitor={...value,id};
 } else {
  if(!monitor?.active||monitor.url!=='http://api:8090/retrieval/query'||monitor.method!=='POST')throw new Error('Monitor drift');
  const headers=JSON.parse(monitor.headers);
  if(![input.old,input.token].includes(headers.Authorization.replace(/^Bearer /,'')))throw new Error('Credential drift');
  if(input.mode==='deliver'){
   headers.Authorization='Bearer '+input.token;
   await ack(socket,'editMonitor',{...monitor,headers:JSON.stringify(headers)});
  }
 }
 const row=await get('SELECT headers,active FROM monitor WHERE id=?',[monitor.id]);
 if(JSON.parse(row.headers).Authorization!=='Bearer '+input.token||row.active!==1)throw new Error('Credential verification failed');
 const beat=await get('SELECT status,time FROM heartbeat WHERE monitor_id=? ORDER BY id DESC LIMIT 1',[monitor.id]);
 socket.close();db.close();console.log(JSON.stringify({monitor_id:monitor.id,credential_verified:true,active:true,heartbeat:beat?{status:beat.status,at:Date.parse(beat.time+'Z')/1000}:null}));
}
main().catch(()=>{db.close();console.error('Development Kuma operation failed; private output suppressed');process.exit(1)});
