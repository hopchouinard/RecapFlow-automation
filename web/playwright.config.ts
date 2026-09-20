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
export default defineConfig({
  testDir: "./e2e",
  use: { baseURL: "http://127.0.0.1:5173" },
  webServer: {
    command: "npm run dev -- --port 5173 --strictPort",
    url: "http://127.0.0.1:5173",
    reuseExistingServer: false,
  },
  reporter: "list",
});
