import { createRequire } from 'node:module';
import { resolve } from 'node:path';
import { execFileSync } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';

const require = createRequire(resolve(process.cwd(), 'frontend/package.json'));
const { chromium } = require('playwright');
const base = process.env.EVIDENCE_BASE_URL || 'http://127.0.0.1:8000';
const browser = await chromium.launch({
  headless: false,
  args: ['--no-sandbox', '--disable-dev-shm-usage', '--start-maximized', '--window-size=1600,1000']
});
try {
  const page = await browser.newPage({ viewport: null });
  await page.goto(base + '/', { waitUntil: 'domcontentloaded' });
  await page.locator('.dealer-card').first().waitFor();
  await page.bringToFront();
  await delay(5000);
  execFileSync('scrot', ['-o', resolve(process.cwd(), '..', 'get_dealers.png')]);
  console.log('Captured the pre-login dealer homepage from ' + base);
} finally {
  await browser.close();
}
