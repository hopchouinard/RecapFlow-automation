import { test, expect } from "@playwright/test";

test("browse preserved meetings and download original Markdown in dark mode", async ({
  page,
}) => {
  const artifact = {
    id: "a".repeat(64),
    name: "community-post.md",
    origin: "output",
    url: "/api/v1/meeting-artifacts/" + "a".repeat(64) + "/content",
  };
  await page.route("**/api/v1/**", async (route) => {
    const path = new URL(route.request().url()).pathname;
    if (path.endsWith("/content"))
      return route.fulfill({
        contentType: "text/plain",
        body: "# Preserved recap\n<script>literal</script>",
      });
    return route.fulfill({
      json: path.endsWith("/me")
        ? { permissions: ["jobs:read", "artifacts:read"] }
        : path.endsWith("/meetings")
          ? {
              items: [
                { date: "2026-09-08", artifacts: [artifact] },
                { date: "2025-02-02", artifacts: [artifact] },
              ],
            }
          : { items: [] },
    });
  });
  await page.emulateMedia({ colorScheme: "dark" });
  await page.goto("/e2e/fixture.html");
  await expect(page.getByRole("heading", { name: "Meetings 2" })).toBeVisible();
  const tree = page.getByRole("navigation", {
    name: "Meetings by year and month",
  });
  await expect(tree.locator("details[open]")).toHaveCount(0);
  await expect(page.getByRole("button", { name: "2026-09-08" })).toBeHidden();
  const year = tree.locator("summary").filter({ hasText: "2025" });
  await expect(page.getByRole("button", { name: "2025-02-02" })).toBeHidden();
  await year.focus();
  await page.keyboard.press("Enter");
  const month = tree.locator("summary").filter({ hasText: "February" });
  await month.click();
  await expect(page.getByRole("button", { name: "2025-02-02" })).toBeVisible();
  await year.click();
  await expect(page.getByRole("button", { name: "2025-02-02" })).toBeHidden();
  await page.getByRole("searchbox").fill("2025");
  await expect(page.getByRole("button", { name: /2026-09-08/ })).toHaveCount(0);
  await page.getByRole("button", { name: /2025-02-02/ }).click();
  await page.getByRole("button", { name: "community-post.md" }).click();
  await expect(page.locator("pre")).toHaveText(
    "# Preserved recap\n<script>literal</script>",
  );
  await expect(page.locator("pre script")).toHaveCount(0);
  await page.getByRole("button", { name: "Rendered", exact: true }).click();
  await expect(
    page.getByRole("heading", { name: "Preserved recap" }),
  ).toBeVisible();
  await expect(page.locator(".markdown-content script")).toHaveCount(0);
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.screenshot({
    animations: "disabled",
    path: "test-results/signal-desktop-dark.png",
    fullPage: true,
  });
  await page.getByRole("switch", { name: "Dark mode" }).click();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "light");
  await page.screenshot({
    animations: "disabled",
    path: "test-results/signal-desktop-light.png",
    fullPage: true,
  });
  await page.setViewportSize({ width: 390, height: 844 });
  expect(
    await page.evaluate(() => document.documentElement.scrollWidth),
  ).toBeLessThanOrEqual(390);
  await page.screenshot({
    animations: "disabled",
    path: "test-results/signal-mobile-light.png",
    fullPage: true,
  });
  await page.getByRole("switch", { name: "Dark mode" }).click();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "dark");
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({
    animations: "disabled",
    path: "test-results/rendered-markdown-mobile.png",
    fullPage: true,
  });
  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Download file" }).click();
  const downloaded = await download;
  expect(downloaded.suggestedFilename()).toBe("community-post.md");
  const stream = await downloaded.createReadStream();
  const chunks = [];
  for await (const chunk of stream!) chunks.push(chunk);
  expect(Buffer.concat(chunks).toString()).toBe(
    "# Preserved recap\n<script>literal</script>",
  );
  await page.getByRole("button", { name: "Raw", exact: true }).click();
  await expect(page.getByLabel("Raw file contents")).toHaveText(
    "# Preserved recap\n<script>literal</script>",
  );
  await page.getByRole("searchbox").fill("");
  await expect(tree.locator("details[open]")).toHaveCount(0);
  await page.setViewportSize({ width: 390, height: 844 });
  expect(
    await page.evaluate(() => document.documentElement.scrollWidth),
  ).toBeLessThanOrEqual(390);
  await page.screenshot({
    animations: "disabled",
    path: "test-results/archive-mobile.png",
    fullPage: true,
  });
});
