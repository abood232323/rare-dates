import { createRequire } from "module";
const require = createRequire(import.meta.url);
const puppeteer = require("C:/Users/abood/Desktop/job offer/node_modules/puppeteer/lib/cjs/puppeteer/puppeteer.js");
import { mkdirSync, readdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const dir = join(__dirname, "temporary screenshots");
mkdirSync(dir, { recursive: true });

const url   = process.argv[2] || "http://localhost:3000";
const label = process.argv[3] || "";

// find next N
const existing = readdirSync(dir).filter(f => f.startsWith("screenshot-")).length;
const n = existing + 1;
const fname = label ? `screenshot-${n}-${label}.png` : `screenshot-${n}.png`;
const outPath = join(dir, fname);

const browser = await puppeteer.launch({
  executablePath: "C:/Users/abood/.cache/puppeteer/chrome/win64-147.0.7727.57/chrome-win64/chrome.exe",
  args: ["--no-sandbox"],
});

const page = await browser.newPage();
await page.setViewport({ width: 794, height: 1123, deviceScaleFactor: 2 });
await page.goto(url, { waitUntil: "networkidle0" });
await page.screenshot({ path: outPath, fullPage: true });
await browser.close();

console.log(`Saved: ${outPath}`);
