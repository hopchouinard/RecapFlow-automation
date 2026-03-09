# Chapter 5 — Credentials & Security

**Category:** Infrastructure & Deployment
**Reading time:** 4 minutes

---

## Credential Management

All API keys and secrets are stored in n8n's encrypted credential store, never in workflow JSON files or environment variables.

### Credentials in Use

| Credential | n8n Type | Service | Purpose |
|-----------|----------|---------|---------|
| Fathom API Key | Header Auth (`X-Api-Key`) | api.fathom.ai | Fetch meeting transcripts |
| OpenRouter API | OpenRouter API | openrouter.ai | LLM inference (Claude Sonnet 4.6) |

### How Credentials Work in n8n

n8n encrypts all credentials at rest using `N8N_ENCRYPTION_KEY`. This key is auto-generated on first startup and stored in `data/config`. Workflow JSON files reference credentials by name and a placeholder ID:

```json
"credentials": {
  "httpHeaderAuth": {
    "id": "PLACEHOLDER",
    "name": "Fathom API Key"
  }
}
```

After importing a workflow, credentials must be linked manually in the n8n UI. This is by design — it prevents credential leakage through workflow exports.

### Critical Warning

**Never delete or modify `data/config`** — it contains the encryption key for all stored credentials. If this key is lost, all credentials must be re-entered. **Never change `N8N_ENCRYPTION_KEY`** after credentials have been saved.

## Security Boundaries

### What Stays Local

- All files (chat logs, transcripts, outputs) remain on the local network
- n8n UI is only accessible on the local network (:5678)
- SSH keys stay on the Mac with passphrase in Keychain
- No inbound connections from the internet

### What Goes External

- **Fathom API** (HTTPS): Polling for new recordings, fetching transcripts
- **OpenRouter API** (HTTPS): Sending merged content for LLM processing

### Data in Transit

The merged transcript + chat log is sent to OpenRouter for LLM processing. This content includes participant names and discussion topics. Consider this when deciding which model provider to use.

## Fathom API Key Setup

1. Go to https://fathom.video/customize#api-access-header
2. Navigate to User Settings → API Access
3. Generate an API key
4. In n8n: Credentials → Add Credential → Header Auth
5. Header Name: `X-Api-Key`
6. Header Value: paste the key

### Rate Limits

Fathom allows 60 requests per 60-second window, per user. The poller runs every 15 minutes with 1-2 requests per cycle, well within limits.

## Re-Import Gotcha

Every time a workflow JSON is re-imported via `n8n import:workflow`, credential links are reset to the placeholder values. You must re-link credentials in the n8n UI after each import. This is a known n8n behavior, not a bug.
