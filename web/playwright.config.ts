import { defineConfig } from "@playwright/test";
import { existsSync } from "node:fs";
import { homedir } from "node:os";
const libs =
  (process.env.XDG_CACHE_HOME || homedir() + "/.cache") +
  "/cbm-test-services/root/usr/lib/x86_64-linux-gnu";
if (existsSync(libs)) process.env.LD_LIBRARY_PATH = libs;
const fonts =
  (process.env.XDG_CACHE_HOME || homedir() + "/.cache") +
  "/cbm-test-services/fonts.conf";
if (existsSync(fonts)) process.env.FONTCONFIG_FILE = fonts;
const devUrl = process.env.CBM_DEV_BROWSER_URL;
if (devUrl && !/^http:\/\/127\.0\.0\.1:\d+$/.test(devUrl)) {
  throw new Error(
    "CBM_DEV_BROWSER_URL must use the loopback SSH tunnel to VM108",
  );
}
export default defineConfig({
  testDir: "./e2e",
  use: { baseURL: devUrl || "http://127.0.0.1:5173" },
  webServer: devUrl
    ? undefined
    : {
        command: "npm run dev -- --port 5173 --strictPort",
        url: "http://127.0.0.1:5173",
        reuseExistingServer: false,
      },
  reporter: "list",
});
