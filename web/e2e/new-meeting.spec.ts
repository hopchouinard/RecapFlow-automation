import { test, expect } from "@playwright/test";

test("manual weekly upload preserves files and explicit meeting metadata", async ({
  page,
}) => {
  const posts: { path: string; body: any }[] = [];
  let job: any;
  await page.route("**/api/v1/**", async (route) => {
    const request = route.request();
    const path = new URL(request.url()).pathname;
    if (request.method() === "POST") {
      const body = request.postDataJSON();
      posts.push({ path, body });
      if (path.endsWith("/sources"))
        return route.fulfill({ json: { id: body.kind } });
      job = {
        ...body,
        id: "new",
        processing: "queued",
        artifacts: "pending",
        indexing: "pending",
        git: "not_requested",
        distribution: "not_requested",
        stages: [],
      };
      return route.fulfill({ status: 202, json: { id: "new" } });
    }
    return route.fulfill({
      json: path.endsWith("/me")
        ? {
            automatic_processing: true,
            processing_readiness: { state: "ready", ready: true },
            permissions: [
              "jobs:read",
              "artifacts:read",
              "jobs:submit",
              "sources:upload",
            ],
          }
        : path.endsWith("/jobs")
          ? { items: job ? [job] : [] }
          : path.endsWith("/meetings") || path.endsWith("/artifacts")
            ? { items: [] }
            : job,
    });
  });
  await page.clock.install();
  await page.goto("/e2e/fixture.html");
  await page.getByRole("button", { name: "New meeting", exact: true }).click();
  await expect(
    page.getByText("Saving starts processing automatically", { exact: false }),
  ).toBeVisible();
  const form = page.getByRole("form", { name: "New meeting" });
  await form
    .getByLabel("Meeting ID", { exact: true })
    .fill("manual-2026-09-15");
  await form.getByLabel("Meeting date and time").fill("2026-09-15T17:30");
  await form.getByLabel("Timezone", { exact: true }).fill("Invalid/Zone");
  await form.getByLabel("Transcript", { exact: true }).setInputFiles({
    name: "transcript.txt",
    mimeType: "text/plain",
    buffer: Buffer.from("Original weekly transcript.\n"),
  });
  await form.getByLabel("Zoom chat", { exact: true }).setInputFiles({
    name: "chat.txt",
    mimeType: "text/plain",
    buffer: Buffer.from("Original Zoom chat.\n"),
  });
  await form.getByRole("button", { name: "Save and process meeting" }).click();
  await expect(page.getByRole("alert")).toContainText("valid timezone");
  expect(posts).toHaveLength(0);
  await form.getByLabel("Timezone", { exact: true }).fill("America/Toronto");
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({
    path: "test-results/new-meeting-mobile.png",
    fullPage: true,
  });
  expect(
    await page.evaluate(() => document.documentElement.scrollWidth),
  ).toBeLessThanOrEqual(390);
  await form.getByRole("button", { name: "Save and process meeting" }).click();
  await expect(form).toHaveCount(0);
  expect(posts).toHaveLength(3);
  expect(posts[0].body.content).toBe("Original weekly transcript.\n");
  expect(posts[1].body.content).toBe("Original Zoom chat.\n");
  expect(posts[2].body).toEqual({
    identity: {
      meeting_id: "manual-2026-09-15",
      started_at: "2026-09-15T21:30:00.000Z",
      timezone: "America/Toronto",
      local_date: "2026-09-15",
      provider: "manual",
    },
    mode: "weekly",
    sources: { transcript: "transcript", chat: "chat" },
    version: "processing-v1",
  });
  await expect(page.getByRole("heading", { name: "2026-09-15" })).toBeVisible();
  job.processing = "succeeded";
  job.artifacts = "ready";
  job.indexing = "complete";
  await page.clock.fastForward(16000);
  await expect(page.locator('.states [data-state="complete"]')).toHaveText(
    "complete",
  );
  expect(posts).toHaveLength(3);
});
