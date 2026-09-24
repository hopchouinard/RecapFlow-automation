// Convert an explicit meeting wall time, independent of the browser's timezone.
export function meetingStart(
  local: string,
  timezone: string,
  offset = "",
): string {
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/.test(local))
    throw new Error("Enter the meeting date and time.");
  let format: Intl.DateTimeFormat;
  try {
    format = new Intl.DateTimeFormat("en-CA", {
      timeZone: timezone,
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      hourCycle: "h23",
    });
  } catch {
    throw new Error("Enter a valid timezone, such as America/Toronto.");
  }
  const wall = (time: number) => {
    const parts = Object.fromEntries(
      format.formatToParts(time).map((p) => [p.type, p.value]),
    );
    return `${parts.year}-${parts.month}-${parts.day}T${parts.hour}:${parts.minute}`;
  };
  const guess = Date.parse(local + ":00Z");
  if (!Number.isFinite(guess)) throw new Error("Enter a valid meeting date.");
  const offsets = new Set(
    [-36, 0, 36].map((hours) => {
      const sample = guess + hours * 3600000;
      return Date.parse(wall(sample) + ":00Z") - sample;
    }),
  );
  let candidates = [...offsets]
    .map((delta) => guess - delta)
    .filter((t) => wall(t) === local);
  if (offset) {
    if (!/^[+-](?:0\d|1\d|2[0-3]):[0-5]\d$/.test(offset))
      throw new Error("Use a UTC offset such as -04:00.");
    const explicit = Date.parse(local + ":00" + offset);
    candidates = candidates.filter((t) => t === explicit);
  }
  if (candidates.length === 0)
    throw new Error(
      "That time or UTC offset does not exist in the selected timezone. Check the meeting time.",
    );
  if (candidates.length > 1)
    throw new Error(
      "That time occurs twice during the daylight-saving change. Enter its UTC offset below.",
    );
  return new Date(candidates[0]).toISOString();
}
