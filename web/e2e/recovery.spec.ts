import { test, expect } from "@playwright/test";

for (const operation of ["upload", "retry"]) {
  test(`failed acquisition ${operation} keeps the same meeting`, async ({
    page,
  }) => {
    const posts: { path: string; body: any }[] = [];
    const job: any = {
      id: "existing",
      identity: { meeting_id: "821559116", local_date: "2026-09-15" },
      mode: "weekly",
      processing: "waiting_for_input",
      acquisition: "failed",
      artifacts: "pending",
      indexing: "pending",
      backup: "not_started",
      git: "not_requested",
      distribution: "not_requested",
      sources: { chat: "chat" },
      missing_inputs: ["transcript"],
      stages: [
        {
          id: "acquisition",
          name: "acquisition",
          state: "failed",
          generation: 1,
          error: "fathom_unavailable",
          retryable: true,
          safe_retryable: true,
        },
      ],
    };
    await page.route("**/api/v1/**", async (route) => {
      const req = route.request(),
        path = new URL(req.url()).pathname;
      if (req.method() === "POST") {
        posts.push({ path, body: req.postDataJSON() });
        if (path === "/api/v1/sources")
          return route.fulfill({ json: { id: "fallback" } });
        job.acquisition = operation === "upload" ? "ready" : "queued";
        job.stages = [];
        if (operation === "upload") {
          job.processing = "queued";
          job.missing_inputs = [];
        }
        return route.fulfill({ status: 202, json: { id: job.id } });
      }
      return route.fulfill({
        json: path.endsWith("/me")
          ? {
              automatic_processing: true,
              permissions: [
                "jobs:read",
                "jobs:submit",
                "sources:upload",
                "artifacts:read",
              ],
            }
          : path.endsWith("/jobs")
            ? { items: [job] }
            : path.endsWith("/meetings") || path.endsWith("/artifacts")
              ? { items: [] }
              : job,
      });
    });
    await page.goto("/e2e/fixture.html");
    await page
      .getByRole("button", { name: "Recent runs", exact: true })
      .click();
    await page.getByRole("button", { name: /2026-09-15/ }).click();
    await expect(
      page.getByText("Fathom could not be reached.", { exact: false }),
    ).toBeVisible();
    await expect(page.getByText("backup", { exact: true })).toBeVisible();
    if (operation === "upload") {
      await page
        .getByLabel("Upload transcript and continue")
        .setInputFiles({
          name: "transcript.txt",
          mimeType: "text/plain",
          buffer: Buffer.from("Fallback transcript"),
        });
      await expect(
        page.getByLabel("Upload transcript and continue"),
      ).toHaveCount(0);
      expect(posts.map((p) => p.path)).toEqual([
        "/api/v1/sources",
        "/api/v1/jobs/existing/sources",
      ]);
      expect(posts[1].body).toEqual({ transcript: "fallback" });
    } else {
      await page
        .getByLabel("Reason for retry or rerun")
        .fill("Fathom is available again");
      await page.getByRole("button", { name: "Retry acquisition" }).click();
      await expect(
        page.getByRole("button", { name: "Retry acquisition" }),
      ).toHaveCount(0);
      expect(posts[0].path).toBe(
        "/api/v1/jobs/existing/stages/acquisition/resume",
      );
      expect(posts[0].body.generation).toBe(1);
    }
    expect(posts.some((p) => p.path === "/api/v1/jobs")).toBe(false);
  });
}
