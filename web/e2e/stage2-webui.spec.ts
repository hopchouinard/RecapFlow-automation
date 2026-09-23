import { test, expect } from '@playwright/test';
import { readFileSync } from 'node:fs';

const credentialsPath = process.env.CBM_STAGE2_CREDENTIALS_FILE;
const recordsPath = process.env.CBM_STAGE2_RECORDS_FILE;
test.skip(!process.env.CBM_DEV_BROWSER_URL || !credentialsPath || !recordsPath,
  'Requires the isolated VM108 Open WebUI fixture and private test inputs');

test('restored Open WebUI renders login and retained synthetic chat', async ({ page }) => {
  const credentials = JSON.parse(readFileSync(credentialsPath!, 'utf8'));
  const records = JSON.parse(readFileSync(recordsPath!, 'utf8'));
  await page.goto('/');
  await expect(page.getByPlaceholder('Enter Your Email')).toBeVisible();
  await expect(page.getByPlaceholder('Enter Your Password')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Sign up' })).toHaveCount(0);
  await page.getByPlaceholder('Enter Your Email').fill(credentials.email);
  await page.getByPlaceholder('Enter Your Password').fill(credentials.password);
  await page.getByRole('button', { name: 'Sign in' }).click();
  await expect(page).not.toHaveURL(/\/auth(?:\?|$)/);
  await page.goto(`/c/${records.chat_id}`);
  await expect(page.getByText('Synthetic only')).toBeVisible();
  await page.reload();
  await expect(page.getByText('Synthetic only')).toBeVisible();
});
