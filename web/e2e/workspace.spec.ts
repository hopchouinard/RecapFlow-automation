import { test, expect } from "@playwright/test";
test("preview and download preserve literal Markdown", async ({ page }) => {
  const job = {
    id: "job",
    identity: { local_date: "2026-09-08", meeting_id: "fixture" },
    mode: "weekly",
    processing: "succeeded",
    artifacts: "ready",
    indexing: "partial",
    git: "failed",
    distribution: "not_requested",
    stages: [],
  };
  await page.route("**/api/v1/**", async (route) => {
    const path = new URL(route.request().url()).pathname;
    if (path.endsWith("/content"))
      return route.fulfill({
        contentType: "text/plain",
        body: "# Recap\nLiteral Markdown.",
      });
    const json = path.endsWith("/me")
      ? { permissions: ["jobs:read", "artifacts:read"] }
      : path.endsWith("/meetings")
        ? { items: [] }
        : path.endsWith("/artifacts")
          ? {
              items: [
                {
                  id: "file",
                  name: "community-post.md",
                  url: "/api/v1/artifacts/file/content",
                },
              ],
            }
          : path.endsWith("/jobs")
            ? { items: [job] }
            : job;
    await route.fulfill({ json });
  });
  await page.emulateMedia({ colorScheme: "dark" });
  await page.goto("/e2e/fixture.html");
  const themeSwitch = page.getByRole("switch", { name: "Dark mode" });
  await expect(themeSwitch).toBeChecked();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
  await themeSwitch.focus();
  await page.keyboard.press("Space");
  await expect(themeSwitch).not.toBeChecked();
  await page.reload();
  await expect(themeSwitch).not.toBeChecked();
  await themeSwitch.click();
  await expect(page.locator("html")).toHaveCSS("color-scheme", "dark");
  await page.getByRole("button", { name: "Recent runs" }).click();
  await page.getByRole("button", { name: /2026-09-08/ }).click();
  await page.screenshot({ path: "test-results/workspace.png", fullPage: true });
  await expect(page.getByText("partial", { exact: true })).toBeVisible();
  await page.getByRole("button", { name: "community-post.md" }).click();
  await expect(page.locator("pre")).toHaveText("# Recap\nLiteral Markdown.");
  await page.screenshot({
    path: "test-results/workspace-dark.png",
    fullPage: true,
  });
  await page.setViewportSize({ width: 390, height: 844 });
  await expect(themeSwitch).toBeVisible();
  expect(
    await page.evaluate(() => document.documentElement.scrollWidth),
  ).toBeLessThanOrEqual(390);
  await page.screenshot({
    path: "test-results/workspace-dark-mobile.png",
    fullPage: true,
  });
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Download file" }).click();
  expect((await download).suggestedFilename()).toBe("community-post.md");
});
