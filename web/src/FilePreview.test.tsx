import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, expect, it } from "vitest";
import { FilePreview } from "./FilePreview";

afterEach(cleanup);

it("toggles GFM rendering while preserving source and preventing active content", () => {
  const text =
    "# Meeting\n\n**Important**\n\n| Topic | Owner |\n| --- | --- |\n| Launch | Pat |\n\n- [x] Done\n\n```js\nconst x = 1;\n```\n\n<script>bad()</script>\n\n[unsafe](javascript:alert%281%29)\n\n![private](https://example.com/tracker.png)";
  const { container } = render(
    <FilePreview name="meeting.md" text={text}>
      {null}
    </FilePreview>,
  );
  expect(screen.getByLabelText("Raw file contents").textContent).toBe(text);
  fireEvent.click(screen.getByRole("button", { name: "Rendered" }));
  expect(screen.getByRole("heading", { name: "Meeting" })).toBeVisible();
  expect(screen.getByRole("table")).toBeVisible();
  expect(screen.getByRole("checkbox")).toBeChecked();
  expect(container.querySelector("script, img, iframe")).toBeNull();
  expect(screen.getByText("unsafe")).not.toHaveAttribute(
    "href",
    expect.stringContaining("javascript:"),
  );
  fireEvent.click(screen.getByRole("button", { name: "Raw" }));
  expect(screen.getByLabelText("Raw file contents").textContent).toBe(text);
});

it("keeps ordinary text files literal", () => {
  render(
    <FilePreview name="chat.txt" text="# Literal chat">
      {null}
    </FilePreview>,
  );
  expect(screen.queryByRole("group", { name: "Markdown view" })).toBeNull();
  expect(screen.getByLabelText("Raw file contents")).toHaveTextContent(
    "# Literal chat",
  );
});
