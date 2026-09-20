export type Stage = {
  id: string;
  name: string;
  state: string;
  generation: number;
  error: string | null;
  retryable: boolean;
  safe_retryable?: boolean;
};
export type Job = {
  id: string;
  identity: {
    meeting_id: string;
    local_date: string;
    started_at: string;
    timezone: string;
    provider: string;
  };
  mode: string;
  version: string;
  sources: Record<string, string>;
  acquisition?: string;
  backup?: string;
  processing: string;
  artifacts: string;
  indexing: string;
  git: string;
  distribution: string;
  stages?: Stage[];
  missing_inputs?: string[];
};
export type Artifact = {
  id: string;
  name: string;
  sha256: string;
  bytes: number;
  url: string;
};
export class Api {
  private pendingKeys = new Map<string, string>();
  constructor(private token: () => Promise<string>) {}
  async request<T>(
    path: string,
    body?: unknown,
    method = body ? "POST" : "GET",
  ): Promise<T> {
    const operation = method + path + JSON.stringify(body);
    if (body && !this.pendingKeys.has(operation))
      this.pendingKeys.set(operation, crypto.randomUUID());
    const result = await fetch("/api/v1" + path, {
      method,
      headers: {
        Authorization: "Bearer " + (await this.token()),
        ...(body
          ? {
              "Content-Type": "application/json",
              "Idempotency-Key": this.pendingKeys.get(operation)!,
            }
          : {}),
      },
      body: body ? JSON.stringify(body) : undefined,
    });
    if (!result.ok) {
      const problem = await result
        .json()
        .catch(() => ({ code: "request_failed" }));
      throw new Error(problem.code.replaceAll("_", " "));
    }
    const value = await result.json();
    this.pendingKeys.delete(operation);
    return value;
  }
  async text(artifact: Artifact) {
    const result = await fetch(artifact.url, {
      headers: { Authorization: "Bearer " + (await this.token()) },
    });
    if (!result.ok)
      throw new Error("Artifact is unavailable or failed verification.");
    return result.text();
  }
}
