import { describe, expect, it } from "vitest";
import { meetingStart } from "./meetingTime";

describe("meeting timezone metadata", () => {
  it("uses the selected timezone independently of browser timezone", () => {
    expect(meetingStart("2026-09-15T17:30", "America/Toronto")).toBe(
      "2026-09-15T21:30:00.000Z",
    );
    expect(meetingStart("2026-01-15T17:30", "America/Toronto")).toBe(
      "2026-01-15T22:30:00.000Z",
    );
    expect(meetingStart("2026-09-15T00:30", "Asia/Kolkata")).toBe(
      "2026-09-14T19:00:00.000Z",
    );
  });
  it("rejects nonexistent or invalid wall times and zones", () => {
    expect(() => meetingStart("2026-03-08T02:30", "America/Toronto")).toThrow(
      "does not exist",
    );
    expect(() => meetingStart("2026-09-15T17:30", "Invalid/Zone")).toThrow(
      "valid timezone",
    );
    expect(() => meetingStart("2026-02-30T17:30", "UTC")).toThrow();
  });
  it("requires an explicit offset for a repeated time", () => {
    expect(() => meetingStart("2026-11-01T01:30", "America/Toronto")).toThrow(
      "occurs twice",
    );
    expect(meetingStart("2026-11-01T01:30", "America/Toronto", "-04:00")).toBe(
      "2026-11-01T05:30:00.000Z",
    );
    expect(meetingStart("2026-11-01T01:30", "America/Toronto", "-05:00")).toBe(
      "2026-11-01T06:30:00.000Z",
    );
    expect(() =>
      meetingStart("2026-09-15T17:30", "America/Toronto", "-05:00"),
    ).toThrow("does not exist");
  });
});
