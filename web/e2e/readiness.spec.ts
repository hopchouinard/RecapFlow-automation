import { test, expect } from "@playwright/test";

test("paused service saves for later and polling reflects recovery and lost status", async ({
  page,
}) => {
  let readiness = { state: "paused", ready: false };
  let unavailable = false;
  let saved: any = null;
  const posts: string[] = [];
  await page.route("**/api/v1/**", async (route) => {
    const req = route.request();
    const path = new URL(req.url()).pathname;
    if (path.endsWith("/me")) {
      if (unavailable) return route.abort();
      return route.fulfill({
        json: {
          permissions: [
            "jobs:read",
            "sources:upload",
            "jobs:submit",
            "artifacts:read",
          ],
          automatic_processing: true,
          processing_readiness: readiness,
        },
      });
    }
    if (req.method() === "POST") {
      posts.push(path);
      if (path.endsWith("/sources"))
        return route.fulfill({ json: { id: req.postDataJSON().kind } });
      saved = {
        ...req.postDataJSON(),
        id: "queued",
        processing: "queued",
        artifacts: "pending",
        indexing: "pending",
        git: "not_requested",
        distribution: "not_requested",
        stages: [],
      };
      return route.fulfill({ status: 202, json: { id: "queued" } });
    }
    return route.fulfill({
      json: path.endsWith("/jobs")
        ? { items: saved ? [saved] : [] }
        : path.endsWith("/meetings") || path.endsWith("/artifacts")
          ? { items: [] }
          : saved,
    });
  });
  await page.clock.install();
  await page.goto("/e2e/fixture.html");
  const availability = page.getByRole("status", {
    name: "Processing availability",
  });
  await expect(availability).toContainText("processing is paused");
  await page.getByRole("button", { name: "New meeting", exact: true }).click();
  await expect(
    page.getByText("Saving starts processing automatically", { exact: false }),
  ).toHaveCount(0);
  const form = page.getByRole("form", { name: "New meeting" });
  await form
    .getByLabel("Meeting ID", { exact: true })
    .fill("readiness-fixture");
  await form.getByLabel("Meeting date and time").fill("2026-09-20T12:00");
  await form.getByLabel("Timezone", { exact: true }).fill("Etc/UTC");
  for (const name of ["Transcript", "Zoom chat"]) {
    await form
      .getByLabel(name, { exact: true })
      .setInputFiles({
        name: "fixture.txt",
        mimeType: "text/plain",
        buffer: Buffer.from("Synthetic input only."),
      });
  }
  await form.getByRole("button", { name: "Save for later processing" }).click();
  await expect(form).toHaveCount(0);
  await expect(
    page.getByText("Meeting saved.", { exact: false }),
  ).toBeVisible();
  expect(posts).toHaveLength(3);
  readiness = { state: "ready", ready: true };
  await page.clock.fastForward(16000);
  await expect(availability).toHaveCount(0);
  await page.getByRole("button", { name: "New meeting", exact: true }).click();
  await expect(
    form.getByRole("button", { name: "Save and process meeting" }),
  ).toBeVisible();
  unavailable = true;
  await page.clock.fastForward(16000);
  await expect(availability).toContainText("status is unavailable");
  await expect(
    form.getByRole("button", { name: "Save for later processing" }),
  ).toBeVisible();
  expect(posts).toHaveLength(3);
});
