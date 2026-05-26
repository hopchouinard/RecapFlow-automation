#!/usr/bin/env bash
# Commit and push weekly call artifacts (output/ + watch/) if any are
# new or modified. Designed to run weekly via cron on Wed 02:00, after
# the Tuesday weekly call has been processed by n8n.
#
# Safe to run more often: exits cleanly with no commit if nothing changed.

set -euo pipefail

REPO="/home/pchouinard/n8n"
BRANCH="main"
LOG_TAG="commit-weekly-artifacts"

log() { logger -t "$LOG_TAG" -- "$*"; echo "[$LOG_TAG] $*"; }

cd "$REPO"

# Refuse to run mid-rebase/merge or on a non-main checkout.
if [[ -d .git/rebase-merge || -d .git/rebase-apply || -f .git/MERGE_HEAD ]]; then
  log "ERROR: repo is mid-rebase/merge; aborting"
  exit 1
fi
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [[ "$current_branch" != "$BRANCH" ]]; then
  log "ERROR: HEAD is on '$current_branch', expected '$BRANCH'; aborting"
  exit 1
fi

# Fast-forward to remote before committing, so we don't accidentally
# diverge if something else landed on origin/main.
log "fetching origin"
git fetch --quiet origin "$BRANCH"
if ! git merge-base --is-ancestor "origin/$BRANCH" HEAD 2>/dev/null \
   && ! git merge-base --is-ancestor HEAD "origin/$BRANCH" 2>/dev/null; then
  log "ERROR: local $BRANCH has diverged from origin/$BRANCH; aborting"
  exit 1
fi
git pull --ff-only --quiet origin "$BRANCH"

# Only look at output/ and watch/. Anything else dirty in the tree is
# someone else's in-progress work and we leave it alone.
changes=$(git status --porcelain -- output/ watch/ || true)
if [[ -z "$changes" ]]; then
  log "no changes in output/ or watch/; nothing to commit"
  exit 0
fi

# Derive the date(s) being committed from new/modified output/<date>/ paths.
# Falls back to today's date if we can't parse one out.
dates=$(echo "$changes" \
  | awk '{print $NF}' \
  | grep -oE 'output/[0-9]{4}-[0-9]{2}-[0-9]{2}' \
  | sed 's|output/||' \
  | sort -u \
  | paste -sd ', ' -)
if [[ -z "$dates" ]]; then
  dates=$(date +%Y-%m-%d)
fi

git add output/ watch/

# If `git add` ended up staging nothing (e.g. only ignored files changed),
# bail out without an empty commit.
if git diff --cached --quiet -- output/ watch/; then
  log "no staged changes after add; nothing to commit"
  exit 0
fi

msg="chore(output): commit ${dates} weekly call artifacts"
log "committing: $msg"
git commit --quiet -m "$msg"

log "pushing to origin/$BRANCH"
if ! git push --quiet origin "$BRANCH"; then
  log "ERROR: push failed; commit is local at $(git rev-parse --short HEAD)"
  exit 1
fi

log "done: $(git rev-parse --short HEAD)"
