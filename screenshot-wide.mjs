// Desktop-width companion to screenshot.mjs (which is used as-is at 794px).
// A luxury desktop site has to be verified at desktop width too.
// Usage: node screenshot-wide.mjs http://localhost:3001 label [width]
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const puppeteer = require("C:/Users/abood/Desktop/job offer/node_modules/puppeteer/lib/cjs/puppeteer/puppeteer.js");
import { mkdirSync, readdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const dir = join(__dirname, "temporary screenshots");
mkdirSync(dir, { recursive: true });

const url   = process.argv[2] || "http://localhost:3001";
const label = process.argv[3] || "wide";
const width = parseInt(process.argv[4] || "1440", 10);

const existing = readdirSync(dir).filter(f => f.startsWith("screenshot-")).length;
const outPath = join(dir, `screenshot-${existing + 1}-${label}.png`);

const browser = await puppeteer.launch({
  executablePath: "C:/Users/abood/.cache/puppeteer/chrome/win64-147.0.7727.57/chrome-win64/chrome.exe",
  args: ["--no-sandbox"],
});

const page = await browser.newPage();
await page.setViewport({ width, height: 900, deviceScaleFactor: 1 });
await page.goto(url, { waitUntil: "networkidle0" });
await page.screenshot({ path: outPath, fullPage: true });
await browser.close();

console.log(`Saved: ${outPath}`);
