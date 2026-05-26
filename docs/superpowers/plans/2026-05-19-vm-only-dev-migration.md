# VM-Only Development Migration Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to walk this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. This is an operational migration, not a code feature — no TDD-style red/green cycles, but every step still has exact commands and explicit validation.

**Goal:** Migrate all RecapFlow-automation development work from the Mac Mini to the n8n VM, eliminating two-clone divergence as a class of problem.

**Architecture:** Single canonical clone on the VM at `~/n8n/`. The Mac Mini becomes a thin IDE host via VS Code Remote SSH and Warp+SSH+Claude Code, with the existing Mac clone frozen as a read-only mirror updated only via `git fetch` (never edited locally). All commits originate on the VM. Operational artifacts (output/, watch/) auto-commit at workflow end via an n8n hook.

**Tech Stack:** Existing — git, ssh, rsync, n8n, Docker Compose, Claude Code, VS Code Remote SSH, Warp.

---

## Pre-conditions

- Both Mac and VM are on `main`, in sync with `origin/main` at `eb73fad` or later. (Confirmed at end of 2026-05-19 session.)
- `tier-b-distribution` branch exists on Mac with 3 unpushed commits.
- Mac `~/.claude/` profile is the authoritative one; VM `~/.claude/` may exist but has not been actively used.

## Success criteria

You can claim this migration done when ALL of the following hold:

1. `tier-b-distribution` work is merged or explicitly archived; no unpushed Mac commits exist.
2. VM `~/.claude/projects/` mirrors Mac's for the RecapFlow-automation project (memory directory + any session state worth preserving).
3. A real Claude Code session run from `ssh` to the VM completes end-to-end work that touches at least one of: retrieval-server `/sessions`, n8n CLI, `docker logs`, LanceDB. (Smoke test, defined in Task 4.)
4. Weekly call workflow auto-commits artifacts at run end without manual intervention; verified on a fresh `/ingest` cycle.
5. Root `CLAUDE.md` reflects VM-only convention; no instructions reference the Mac as a dev location.
6. Mac clone is marked read-only and convention says future edits happen only on the VM. (Solo developer; no verification window — once decided, applied.)

## Rollback

If at any point the migration looks worse than the prior two-clone setup:

- Tasks 1-3 are reversible by inspection (no destructive operations on Mac).
- Task 4 (smoke test) is the decision gate — if Claude Code on VM is unworkable, stop here and keep both clones.
- Task 5 (n8n hook) is fully revertible by removing the appended workflow node.
- Task 6 (CLAUDE.md) is a single revert commit.
- Task 7 (Mac freeze) is a discipline change, not a technical one — start using Mac again any time.

---

## Task 1: Resolve tier-b-distribution branch

**Files:**
- Push: branch `tier-b-distribution` from Mac to origin
- Create: PR via GitHub

Same workflow as the PR we just merged (#2). Decision point at the end: merge or close.

- [ ] **Step 1: Verify branch state on Mac**

```
git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation log --oneline tier-b-distribution ^main
```

Expected: 3 commits — CI cross-repo PR workflow, filter+inference auto-sync, Tier B final-review fixes.

- [ ] **Step 2: Push branch to origin from Mac**

```
git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation push -u origin tier-b-distribution
```

- [ ] **Step 3: Open PR**

```
gh pr create --repo hopchouinard/RecapFlow-automation --base main --head tier-b-distribution --title "feat(ci): Tier B distribution — cross-repo PR workflow + filter sync" --body "<describe the 3 commits>"
```

Or use the GitHub UI if you'd rather hand-write the body.

- [ ] **Step 4: Review + merge the PR**

Standard PR review. Address any Copilot comments using the same pattern as PR #2.

- [ ] **Step 5: Post-merge sync**

On Mac:
```
git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation switch main
git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation pull --ff-only origin main
git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation branch -d tier-b-distribution
git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation push origin --delete tier-b-distribution
```

On VM:
```
ssh n8n-automation.patchoutech.lab "cd ~/n8n && git pull --ff-only origin main"
```

**Validation:** `git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation status -sb` shows `## main...origin/main` with no `ahead`/`behind`. Same on VM.

---

## Task 2: Pre-flight inventory of Mac ~/.claude/

**Files:** Read-only inspection of Mac `~/.claude/`. Output is a manifest used by Task 3.

We need to know exactly what's there before copying it. Surprises during rsync are bad.

- [ ] **Step 1: List top-level structure**

```
ls -la /Users/pchouinard/.claude/
```

Note: `projects/`, `plugins/`, `settings.json`, any other files/dirs.

- [ ] **Step 2: Inventory memory directory for THIS project**

```
ls -la /Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/
wc -l /Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/MEMORY.md
ls /Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/*.md | wc -l
```

Expected: 1 MEMORY.md (the index) + ~15-20 individual memory files. Capture the count for cross-check after migration.

- [ ] **Step 3: List installed skills/plugins**

```
ls /Users/pchouinard/.claude/plugins/cache/ 2>/dev/null
```

Expected: directories like `claude-plugins-official`, possibly others. These hold installed plugins/skills (superpowers, codex, claude-speak, etc.).

- [ ] **Step 4: Capture settings.json**

```
cat /Users/pchouinard/.claude/settings.json 2>/dev/null
```

Take note of permissions, env vars, hook configurations. These don't auto-transfer.

- [ ] **Step 5: List MCP servers**

```
grep -l mcp /Users/pchouinard/.claude/settings.json 2>/dev/null
ls /Users/pchouinard/.claude/mcp-* 2>/dev/null
```

Note any MCP server configs (Google Drive, context7, playwright, server-time, etc.). These need re-configuration on the VM if you use them there.

- [ ] **Step 6: Note what NOT to copy**

The path `-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation` in `projects/` is Mac-specific. On VM, the equivalent project directory name will derive from the VM's path (`/home/pchouinard/n8n` → encoded form). The memory directory contents are portable, but the directory name needs renaming during migration.

**Validation:** You can answer "what's on Mac that I need to recreate on VM?" with a concrete list.

---

## Task 3: Migrate Claude profile to VM

**Files:**
- Source: `/Users/pchouinard/.claude/` (Mac)
- Destination: `/home/pchouinard/.claude/` (VM)

This is the highest-risk step. Memory divergence is hard to detect later. Do this carefully.

- [ ] **Step 1: Determine VM project directory name**

Claude Code derives the project directory name from the working directory path with `/` replaced by `-`. If the VM clone is at `/home/pchouinard/n8n`, the encoded name is `-home-pchouinard-n8n`.

```
ssh n8n-automation.patchoutech.lab "ls /home/pchouinard/.claude/projects/ 2>/dev/null"
```

If a directory like `-home-pchouinard-n8n` already exists, note its contents. If not, it'll be created on first Claude Code run there.

- [ ] **Step 2: Stop any active Claude Code sessions on either side**

You should not be running Claude Code during the migration. Close active sessions on both Mac and VM.

- [ ] **Step 3: Rsync memory directory to VM with renamed target**

```
rsync -av --dry-run /Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/ n8n-automation.patchoutech.lab:/home/pchouinard/.claude/projects/-home-pchouinard-n8n/memory/
```

Review the dry-run output. If correct, run for real:

```
rsync -av /Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/ n8n-automation.patchoutech.lab:/home/pchouinard/.claude/projects/-home-pchouinard-n8n/memory/
```

- [ ] **Step 4: Verify counts match**

```
ls /Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/*.md | wc -l
ssh n8n-automation.patchoutech.lab "ls /home/pchouinard/.claude/projects/-home-pchouinard-n8n/memory/*.md | wc -l"
```

Expected: identical counts.

- [ ] **Step 5: Spot-check MEMORY.md contents**

```
diff /Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/MEMORY.md <(ssh n8n-automation.patchoutech.lab "cat /home/pchouinard/.claude/projects/-home-pchouinard-n8n/memory/MEMORY.md")
```

Expected: no output (files identical).

- [ ] **Step 6: Copy settings.json if it has meaningful content**

```
scp /Users/pchouinard/.claude/settings.json n8n-automation.patchoutech.lab:/home/pchouinard/.claude/settings.json.from-mac
```

DO NOT overwrite the VM's settings.json directly. Land it as `.from-mac` so you can manually merge.

- [ ] **Step 7: Manually merge settings.json**

SSH to VM, open `~/.claude/settings.json` and `~/.claude/settings.json.from-mac`, merge anything you actually want from Mac into the VM file. Most permissions and hooks are environment-specific and you may NOT want them all to carry over. Be deliberate.

- [ ] **Step 8: Note MCP/plugin/skill installations as deferred**

Plugins (superpowers, codex, claude-speak, claude-code-guide) are typically installed via Claude Code's plugin mechanism, not file copy. Document which ones you actively use; install on VM via the normal flow when you start using Claude on VM.

**Validation:** Memory file counts match, MEMORY.md content identical, settings.json merge decisions made consciously.

---

## Task 4: Smoke test Claude Code on VM

**Files:** None modified. This is a behavioral validation.

This is the decision gate. If Claude Code on VM doesn't feel native, the migration stops here.

- [ ] **Step 1: SSH to VM via Warp**

```
ssh n8n-automation.patchoutech.lab
cd ~/n8n
```

- [ ] **Step 2: Launch Claude Code on the VM**

```
claude
```

(Or however your install invokes it. Confirm it starts in the `~/n8n` directory.)

- [ ] **Step 3: Verify it sees the migrated memory**

Ask Claude: "What do you remember about this project?" — it should reference items from the migrated MEMORY.md. If it doesn't recall any of the prior memory, the project-directory naming is wrong.

- [ ] **Step 4: Run a representative task**

Pick something that exercises the VM-local advantages. Example: "Query the retrieval server for sessions from May 2026 and tell me the chunk counts." Claude should run `curl http://10.1.30.10:8999/sessions` locally with no SSH wrapper.

Time it subjectively. If file reads, docker commands, curl calls feel as snappy as you expected, you're good.

- [ ] **Step 5: Test VS Code Remote SSH (optional but recommended)**

From Mac, open VS Code, connect to VM via Remote SSH, open `/home/pchouinard/n8n/`. Edit a file, save, run a test. Confirm the experience is acceptable.

**Validation:** Subjective — does this feel as good or better than the Mac-side experience? If yes, proceed. If no, file a bug for yourself and either fix it or roll back the migration.

---

## Task 5: n8n auto-commit hook for weekly artifacts ✅ DONE (2026-05-26)

**Implementation chosen:** neither Option A nor Option B as originally written. Picked a simpler variant — a host-side cron job that polls for any uncommitted state under `output/` or `watch/` and commits it. No sentinel file, no in-workflow signal, no container changes.

- Script: `scripts/commit-weekly-artifacts.sh`
- Schedule: `30 6 * * 3` (Wed 02:30 EDT / 06:30 UTC), offset 30 min from the existing daily snapshot cron at 02:00 EDT
- Log: `/home/pchouinard/recapflow-logs/commit-weekly-artifacts.log`
- Idempotent: bails out cleanly when there's nothing to commit; refuses to run mid-rebase/merge or off `main`; only stages `output/` and `watch/`, never `-A`
- Auth: relies on existing `gh`-managed HTTPS credentials on the VM

Pending validation: first real fire-off after the Tuesday weekly call (Step 4 below).


**Files:**
- Modify: `workflows/merged-call-summarizer.json` (n8n workflow id 5)

After the Plan B `/ingest` step succeeds, the workflow should trigger a git commit + push for the artifacts it just produced, so weekly outputs land on `main` without manual intervention.

> **Note:** This task could split into its own follow-up plan if you want more design thought (commit-message templating, retry behavior, what to do if push fails). The version below is intentionally simple — add it, observe one weekly run, refine if needed.

**Design wrinkle to resolve before coding:** n8n runs in a Docker container. The host's git checkout (`~/n8n` on the VM) is not directly accessible from inside the container unless mounted. Pick one of:

- **Option A — Bind-mount the repo into n8n:** Add `~/n8n:/host-repo` to the n8n container's volumes in `docker-compose.yml`. The Code node uses Node's built-in process APIs to run `git` commands in `/host-repo`. Requires giving n8n container an SSH key for the GitHub push.
- **Option B — Sentinel + host-side timer:** The workflow writes a `.commit-pending` sentinel file into `output/<date>/`. A separate VM-side systemd timer (or cron, every 5 minutes) detects the sentinel, runs git on the host, deletes the sentinel.

Option B is cleaner: no credentials inside the container, no extra mount, decoupled timing. Recommend Option B unless you have a strong reason for synchronous commit.

- [ ] **Step 1: Snapshot the workflow JSON before editing**

```
ssh n8n-automation.patchoutech.lab "cd ~/n8n && cp workflows/merged-call-summarizer.json /tmp/merged-call-summarizer.json.bak"
```

- [ ] **Step 2: Identify the insertion point**

The workflow currently ends with the `/ingest` POST step. The auto-commit must run AFTER `/ingest` succeeds (and AFTER the ingest-error-log conditional branch). Find the terminal node.

```
grep -E '"name":|"type":' workflows/merged-call-summarizer.json | tail -20
```

- [x] **Step 3: Implement chosen option** (host-side cron variant — see Task 5 header)

**For Option B (recommended):**

- Add a Code node at the end of the workflow that writes `output/<date>/.commit-pending` containing a single line with the date.
- Create `scripts/commit-artifacts-on-sentinel.sh` on the VM that scans `~/n8n/output/*/.commit-pending`, for each one runs `git add output/<date>/ watch/<date>-*`, commits, pushes, and removes the sentinel.
- Create a systemd user timer (or root cron entry, depending on git credential location) running every 5 minutes that invokes the script.

**For Option A:**

- Edit `docker-compose.yml` to bind-mount `~/n8n` as `/host-repo` on the n8n container.
- Provide an SSH deploy key for the container (read+write to RecapFlow-automation).
- Add a Code node that runs git commands inside `/host-repo` via Node's process APIs.

Either path: keep the implementation small (single script or single Code node, no clever retry logic in v1).

- [ ] **Step 4: Test on next weekly call OR force a re-run of 2026-05-19**

Verify the artifacts auto-commit + auto-push without manual intervention.

**Validation:** A fresh weekly run produces a commit on `origin/main` for `output/<date>/` and `watch/<date>-*` without you touching git.

---

## Task 6: Update root CLAUDE.md for VM-only convention ✅ DONE (2026-05-26)

**Files:**
- Modify: `CLAUDE.md` (root)

- [x] **Step 1: Identify Mac-references to remove or rewrite**

```
grep -n "Mac\|mac\|local copy\|Mac Mini\|/Volumes" CLAUDE.md
```

Review each hit. Most can be deleted; some need rewording (e.g., "Mac sync" section becomes "Manual chat-file copy to VM watch/" or similar).

- [x] **Step 2: Add a "Development model" section near the top**

Sample text:

```
## Development model

All RecapFlow-automation development happens on the n8n VM
(`n8n-automation.patchoutech.lab`) at `~/n8n/`. Code edits, git
commits, Claude Code sessions, and PR creation all originate
there. A second clone exists at
`/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation` on the
Mac Mini but is a read-only mirror — updated only via `git fetch`
and `git pull`, never edited locally. Weekly call artifacts
auto-commit to `main` at the end of Workflow 5 via an n8n
post-ingest step.
```

- [x] **Step 3: Commit the CLAUDE.md change**

```
ssh n8n-automation.patchoutech.lab "cd ~/n8n && git add CLAUDE.md && git commit -m 'docs(CLAUDE): document VM-only development model' && git push origin main"
```

- [x] **Step 4: Pull on Mac so the read-only mirror reflects the new doc**

```
git -C /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation pull --ff-only origin main
```

**Validation:** Open the file on both sides; identical content; new section present.

---

## Task 7: Mac clone freeze marker ✅ DONE (2026-05-26, on Mac)

**Files:** None modified in the repo. One local-only marker file added (gitignored via `.git/info/exclude`).

- [x] **Step 1: Add the read-only marker**

```
echo "This clone is read-only. Edit on the VM instead." > /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/.MAC-CLONE-READ-ONLY
echo ".MAC-CLONE-READ-ONLY" >> /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/.git/info/exclude
```

Using `.git/info/exclude` instead of `.gitignore` because the marker is local-only and we don't want it tracked in repo state.

**Validation:** Marker file exists and is gitignored. `git status` on Mac doesn't show it.

---

## Self-review checklist

- All 7 user-agreed migration items covered? Yes (Task 1 through Task 7).
- Memory migration risk surfaced? Yes (Task 3 step 5 + step 7).
- Smoke-test gate explicit? Yes (Task 4 is the decision point).
- Auto-commit design ambiguity flagged? Yes (Task 5 design wrinkle section, two options).
- Rollback path documented? Yes (top of plan).
- Success criteria measurable? Yes (6 explicit criteria, all one-shot).
