import { createRequire } from 'node:module';
import { resolve } from 'node:path';
import { execFileSync } from 'node:child_process';
import { setTimeout as delay } from 'node:timers/promises';

const require = createRequire(resolve(process.cwd(), 'server/frontend/package.json'));
const { chromium } = require('playwright');
const base = (process.env.DEPLOYMENT_URL || '').replace(/\/+$/, '');
const outputDir = process.cwd();
const userSuffix = process.env.GITHUB_RUN_ID || String(Date.now());
const username = ('capstone' + userSuffix).slice(0, 30);
const password = process.env.EVIDENCE_USER_PASSWORD;

if (!base || !/^https?:\/\//i.test(base)) throw new Error('Provide a valid deployed URL through DEPLOYMENT_URL.');
if (!password) throw new Error('EVIDENCE_USER_PASSWORD must be set to a per-run random value.');

const browser = await chromium.launch({ headless: false, args: ['--no-sandbox', '--disable-dev-shm-usage', '--start-maximized', '--window-size=1600,1000'] });
const context = await browser.newContext({ viewport: null });
const page = await context.newPage();
page.setDefaultTimeout(25000);

async function snap(name) {
  await delay(1000);
  execFileSync('scrot', ['-o', resolve(outputDir, name)]);
  console.log('Captured ' + name + ' from ' + base);
}

try {
  const health = await page.request.get(base + '/djangoapp/api/dealers/');
  if (!health.ok()) throw new Error('Dealer API is not healthy at the supplied deployment URL (HTTP ' + health.status() + ').');
  await page.goto(base + '/', { waitUntil: 'domcontentloaded' });
  await page.locator('.dealer-card').first().waitFor();
  await page.evaluate(() => window.scrollTo(0, 0));
  await snap('deployed_landingpage.png');

  const registration = await page.request.post(base + '/djangoapp/api/register/', {
    data: { username, first_name: 'Capstone', last_name: 'Evidence', email: username + '@example.com', password }
  });
  if (registration.status() !== 201) {
    throw new Error('Could not create a temporary evidence account: HTTP ' + registration.status() + ' ' + await registration.text());
  }

  await page.goto(base + '/login/', { waitUntil: 'domcontentloaded' });
  await page.locator('input[name="username"]').fill(username);
  await page.locator('input[name="password"]').fill(password);
  await page.getByRole('button', { name: /log in/i }).click();
  await page.waitForURL(url => url.pathname === '/');
  await page.getByText('Hi, ' + username).waitFor();
  await snap('deployed_loggedin.png');

  await page.goto(base + '/dealer/1/', { waitUntil: 'domcontentloaded' });
  await page.locator('.detail-info h1').waitFor();
  await snap('deployed_dealer_detail.png');

  const reviewText = 'Capstone deployment verification run ' + userSuffix + ': Fantastic services.';
  await page.goto(base + '/dealer/1/review/', { waitUntil: 'domcontentloaded' });
  await page.locator('textarea[name="review"]').fill(reviewText);
  await page.locator('select[name="rating"]').selectOption('5');
  await page.getByRole('button', { name: /post review/i }).click();
  await page.waitForURL(url => url.pathname === '/dealer/1/');
  await page.getByText(reviewText).waitFor();
  await snap('deployed_add_review.png');
} finally {
  await browser.close();
}
