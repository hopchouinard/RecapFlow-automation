import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { App } from "./App";
import { Api } from "./api";

describe("recap workspace", () => {
  it("keeps partial indexing visible and renders artifact content as text", async () => {
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
    const api = new Api(async () => "fixture");
    vi.spyOn(api, "request").mockImplementation(async (path) =>
      path === "/me"
        ? { permissions: ["jobs:read", "artifacts:read"] }
        : path === "/meetings"
          ? { items: [] }
          : path === "/jobs"
            ? { items: [job] }
            : path.endsWith("/artifacts")
              ? {
                  items: [
                    {
                      id: "artifact",
                      name: "community-post.md",
                      url: "/content",
                    },
                  ],
                }
              : job,
    );
    vi.spyOn(api, "text").mockResolvedValue(
      "<script>bad()</script>\n# Community post",
    );
    render(<App api={api} logout={() => {}} />);
    fireEvent.click(screen.getByRole("button", { name: "Recent runs" }));
    fireEvent.click(await screen.findByRole("button", { name: /2026-09-08/ }));
    expect(await screen.findByText("partial")).toBeVisible();
    expect(screen.getByText(/Git publication: failed/)).toBeVisible();
    fireEvent.click(
      await screen.findByRole("button", { name: "community-post.md" }),
    );
    await waitFor(() => expect(screen.getByText(/<script>bad/)).toBeVisible());
    expect(document.querySelector(".preview script")).toBeNull();
    expect(screen.queryByRole("button", { name: "New meeting" })).toBeNull();
  });
});
