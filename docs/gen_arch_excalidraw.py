#!/usr/bin/env python3
"""Generate an Excalidraw file for the RecapFlow + Community Brain architecture.

Layout philosophy (v2 — clean lanes, no crossings):
  - External AI services on TOP row
  - Sources on LEFT column
  - VM container in CENTER, with three vertical sub-columns:
        n8n  →  ./output (shared)  →  retrieval-server
  - Arrows are orthogonal (multi-segment L-paths)
  - "Routing lanes" carved out for cross-container flows:
       y=275-295  → cross-container API calls (POST /ingest)
       Above y=300 → external AI calls (vertical UP into top row)
"""
import json
import random
import time

random.seed(42)
NOW = int(time.time() * 1000)


def _seed():
    return random.randint(1, 2**31 - 1)


def rect(eid, x, y, w, h, *, fill="#ffffff", stroke="#1e1e1e", stroke_width=2,
         dashed=False, group=None, rounded=True):
    return {
        "id": eid,
        "type": "rectangle",
        "x": x, "y": y, "width": w, "height": h,
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": fill,
        "fillStyle": "solid",
        "strokeWidth": stroke_width,
        "strokeStyle": "dashed" if dashed else "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [group] if group else [],
        "frameId": None,
        "roundness": {"type": 3} if rounded else None,
        "seed": _seed(),
        "version": 1,
        "versionNonce": _seed(),
        "isDeleted": False,
        "boundElements": [],
        "updated": NOW,
        "link": None,
        "locked": False,
    }


def text(eid, x, y, w, h, content, *, size=16, align="left", valign="top",
         color="#1e1e1e", container=None, group=None, bold=False):
    font = 5  # Excalifont
    return {
        "id": eid,
        "type": "text",
        "x": x, "y": y, "width": w, "height": h,
        "angle": 0,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2 if bold else 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [group] if group else [],
        "frameId": None,
        "roundness": None,
        "seed": _seed(),
        "version": 1,
        "versionNonce": _seed(),
        "isDeleted": False,
        "boundElements": None,
        "updated": NOW,
        "link": None,
        "locked": False,
        "fontSize": size,
        "fontFamily": font,
        "text": content,
        "textAlign": align,
        "verticalAlign": valign,
        "containerId": container,
        "originalText": content,
        "lineHeight": 1.25,
        "baseline": int(size * 0.85),
    }


def arrow(eid, points, *, color="#1e1e1e", dashed=False, stroke_width=2,
          two_way=False):
    """Multi-segment arrow. `points` is a list of (x,y) absolute coords."""
    x0, y0 = points[0]
    rel = [[p[0] - x0, p[1] - y0] for p in points]
    xs = [p[0] - x0 for p in points]
    ys = [p[1] - y0 for p in points]
    return {
        "id": eid,
        "type": "arrow",
        "x": x0, "y": y0,
        "width": max(xs) - min(xs),
        "height": max(ys) - min(ys),
        "angle": 0,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": stroke_width,
        "strokeStyle": "dashed" if dashed else "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,  # straight segments
        "seed": _seed(),
        "version": 1,
        "versionNonce": _seed(),
        "isDeleted": False,
        "boundElements": None,
        "updated": NOW,
        "link": None,
        "locked": False,
        "startBinding": None,
        "endBinding": None,
        "lastCommittedPoint": None,
        "startArrowhead": "arrow" if two_way else None,
        "endArrowhead": "arrow",
        "points": rel,
    }


def label(eid, x, y, content, *, size=12, color="#5f3dc4"):
    w = max(60, int(len(content.split("\n")[0]) * size * 0.55))
    h = int(size * 1.4 * (content.count("\n") + 1))
    return text(eid, x, y, w, h, content, size=size, align="left", color=color)


# ---------- palette ----------
C_EXTERNAL = "#ffec99"
C_VM = "#f8f9fa"
C_N8N = "#d0ebff"
C_RETRIEVAL = "#d3f9d8"
C_VOLUME = "#ffe8cc"
C_WORKFLOW = "#ffffff"
C_ENDPOINT = "#fff5f5"
C_DB = "#e7f5ff"
C_CONSUMER = "#fff0f6"
C_SHARED = "#fff3bf"

elements = []

# =====================================================================
# TOP ROW — External AI services + consumer (y=60-200)
# =====================================================================
# OpenRouter sits ABOVE n8n (which calls it most heavily)
elements += [
    rect("or-box", 480, 60, 380, 130, fill=C_EXTERNAL),
    text("or-t", 490, 70, 360, 26, "OpenRouter", size=20, bold=True, align="center"),
    text("or-b", 495, 100, 370, 80,
         "Claude Sonnet 4.6\n"
         "All LLM calls (n8n workflows + retrieval Stage B/C)\n"
         "10-min timeout per request",
         size=12, align="center"),
]

# Ollama sits ABOVE retrieval-server (which uses it for embeddings)
elements += [
    rect("ollama-box", 1380, 60, 320, 130, fill=C_EXTERNAL),
    text("ollama-t", 1390, 70, 300, 26, "Ollama (VM host)", size=20, bold=True, align="center"),
    text("ollama-b", 1395, 100, 310, 80,
         "nomic-embed-text\n"
         "via host.docker.internal\n"
         "(extra_hosts in compose)",
         size=12, align="center"),
]

# Open WebUI consumer — top-right
elements += [
    rect("owui-box", 1820, 60, 280, 130, fill=C_CONSUMER),
    text("owui-t", 1830, 70, 260, 26, "Open WebUI", size=20, bold=True, align="center"),
    text("owui-b", 1835, 100, 270, 80,
         "community_brain_filter.py\n"
         "→ POST /query\n"
         "renders ground_truth chunks",
         size=12, align="center"),
]

# =====================================================================
# LEFT COLUMN — Source producers (y=480+)
# =====================================================================
elements += [
    rect("mac-box", 40, 480, 320, 140, fill=C_EXTERNAL),
    text("mac-t", 50, 492, 300, 26, "Mac Mini", size=20, bold=True, align="center"),
    text("mac-b", 55, 525, 310, 90,
         "Zoom client → ~/Documents/Zoom/\n"
         "Automator Folder Action\n"
         "→ sync-zoom-chats.sh\n"
         "→ rsync (ssh) to VM",
         size=12),
]

elements += [
    rect("fathom-box", 40, 660, 320, 110, fill=C_EXTERNAL),
    text("fathom-t", 50, 672, 300, 26, "Fathom API", size=20, bold=True, align="center"),
    text("fathom-b", 55, 705, 310, 60,
         "GET /meetings    GET /transcript\n"
         "(paginated, default 10)\n"
         "polled every 15 min",
         size=12),
]

# =====================================================================
# VM container outer box (y=240-1440, x=400-2100)
# =====================================================================
VM_X, VM_Y, VM_W, VM_H = 400, 240, 1700, 1200
elements += [
    rect("vm-box", VM_X, VM_Y, VM_W, VM_H, fill=C_VM, stroke="#495057",
         stroke_width=3, dashed=True),
    # Title bbox shrunk to actual text width so a-n8n-or (vertical at x=830)
    # passes to the right of it cleanly.
    text("vm-t", VM_X + 20, VM_Y + 12, 400, 28,
         "VM: n8n-automation.patchoutech.lab",
         size=20, bold=True),
    text("vm-sub", VM_X + 20, VM_Y + 42, 400, 20,
         "(Docker Compose)", size=14, color="#495057"),
]

# (Routing-lane meta-label removed — was sitting in the very lane it described.)

# =====================================================================
# n8n container (left-of-VM)
# =====================================================================
N8N_X, N8N_Y, N8N_W, N8N_H = 420, 300, 660, 1120
elements += [
    rect("n8n-box", N8N_X, N8N_Y, N8N_W, N8N_H, fill=C_N8N, stroke="#1971c2",
         stroke_width=2),
    # Title bounding box shrunk to actual text width so the over-the-top
    # /ingest arrows (vertical at x=1060, x=1080) don't pass through it.
    text("n8n-t", N8N_X + 15, N8N_Y + 10, 510, 28,
         "n8n container :5678  (n8nio/n8n:latest, v2.15.1)",
         size=18, bold=True),
]

WX = 440  # workflow content x
WW = 620  # workflow content width

# Volumes at top (these are where data ENTERS n8n)
elements += [
    rect("vol-watch", WX, 350, WW, 60, fill=C_VOLUME),
    text("vol-watch-t", WX + 10, 358, WW - 20, 50,
         "./watch  →  /home/node/watch  (rw)\n"
         "incoming chat + transcript files",
         size=11),

    rect("vol-hist", WX, 420, WW, 60, fill=C_VOLUME),
    text("vol-hist-t", WX + 10, 428, WW - 20, 50,
         "./historical  →  /home/node/historical  (READ-ONLY)\n"
         "~130 backlog Fathom session folders",
         size=11),
]

# Workflows
elements += [
    rect("wf-poller", WX, 510, WW, 80, fill=C_WORKFLOW),
    text("wf-poller-t", WX + 10, 518, WW - 20, 22,
         "Fathom Transcript Poller (id=2)", size=14, bold=True),
    text("wf-poller-b", WX + 10, 542, WW - 20, 50,
         "Schedule Trigger: every 15 min\n"
         "→ writes ./watch/<date>-transcript.txt",
         size=11),
]

elements += [
    rect("wf-merged", WX, 610, WW, 180, fill=C_WORKFLOW),
    text("wf-merged-t", WX + 10, 618, WW - 20, 22,
         "Merged Call Summarizer (id=5) — W1", size=14, bold=True),
    text("wf-merged-b", WX + 10, 642, WW - 20, 150,
         "Trigger: Local File Trigger on ./watch/  (rendezvous)\n"
         "→ Validate + Merge zoom-chat + transcript\n"
         "→ LLM × 5: Signal · Post · Compressed · Invite · Prep\n"
         "→ Save ./output/<YYYY-MM-DD>/*.md\n"
         "→ POST /ingest    (Plan B wired)",
         size=11),
]

elements += [
    rect("wf-trans", WX, 810, WW, 180, fill=C_WORKFLOW),
    text("wf-trans-t", WX + 10, 818, WW - 20, 22,
         "Transcript-Only Summarizer (id=6) — W2", size=14, bold=True),
    text("wf-trans-b", WX + 10, 842, WW - 20, 150,
         "Trigger: Manual (historical backfill)\n"
         "→ Read ./historical/<folder>/transcript\n"
         "→ LLM × 3: Prep-Prompt · Signal · Post\n"
         "→ Save ./output/<YYYY-MM-DD>/*.md\n"
         "→ POST /ingest",
         size=11),
]

elements += [
    rect("wf-helpers", WX, 1010, WW, 80, fill=C_WORKFLOW),
    text("wf-helpers-t", WX + 10, 1018, WW - 20, 22,
         "Diagnostic / utility workflows", size=14, bold=True),
    text("wf-helpers-b", WX + 10, 1042, WW - 20, 50,
         "Fathom: List Recordings (id=3)    Fathom: Fetch Transcript (id=4)\n"
         "Zoom Chat Summarizer (id=1, inactive)",
         size=11),
]

elements += [
    rect("pg-box", WX, 1110, WW, 90, fill=C_DB),
    text("pg-t", WX + 10, 1118, WW - 20, 22,
         "PostgreSQL n8n_db  (postgres:17)", size=14, bold=True),
    text("pg-b", WX + 10, 1142, WW - 20, 60,
         "Workflows · Credentials · Execution history\n"
         "Volume: db_data    (NEVER pin to :latest — v18 breaks layout)",
         size=11),
]

elements += [
    rect("vol-other", WX, 1220, WW, 80, fill=C_VOLUME),
    text("vol-other-t", WX + 10, 1228, WW - 20, 22,
         "Other n8n volumes", size=14, bold=True),
    text("vol-other-b", WX + 10, 1252, WW - 20, 50,
         "./data → /home/node/.n8n  (encryption key, binary data)\n"
         "./n8n-state → /home/node/n8n-state  (poll cursors)",
         size=11),
]

# =====================================================================
# Shared ./output column (between containers)
# =====================================================================
OUT_X, OUT_Y, OUT_W, OUT_H = 1100, 300, 160, 1120
elements += [
    rect("out-box", OUT_X, OUT_Y, OUT_W, OUT_H, fill=C_SHARED, stroke="#a05a00",
         stroke_width=2, dashed=True),
    text("out-t", OUT_X + 10, OUT_Y + 16, OUT_W - 20, 24,
         "./output", size=18, bold=True, align="center", color="#a05a00"),
    text("out-sub", OUT_X + 10, OUT_Y + 50, OUT_W - 20, 80,
         "shared\nvolume", size=14, align="center", color="#a05a00"),
    text("out-b", OUT_X + 10, OUT_Y + 540, OUT_W - 20, 240,
         "n8n: rw\n\n"
         "retrieval-server:\nREAD-ONLY\n\n"
         "<YYYY-MM-DD>/\n"
         "  prepared-\n  transcript.md\n"
         "  extracted-\n  signal.md\n"
         "  community-\n  post.md",
         size=11, align="center", color="#a05a00"),
]

# =====================================================================
# retrieval-server container (right-of-VM)
# =====================================================================
RS_X, RS_Y, RS_W, RS_H = 1280, 300, 800, 1120
elements += [
    rect("rs-box", RS_X, RS_Y, RS_W, RS_H, fill=C_RETRIEVAL, stroke="#2f9e44",
         stroke_width=2),
    # Title moved to the RIGHT side of the container so the /ingest entry
    # verticals (at x=1289 and x=1285) don't pass through its bounding box.
    text("rs-t", 1660, RS_Y + 10, 400, 28,
         "retrieval-server  :127.0.0.1:8999  (community-brain)",
         size=18, bold=True, align="right"),
]

# Endpoints panel (top of retrieval-server)
EP_X, EP_Y, EP_W, EP_H = 1300, 350, 380, 280
elements += [
    rect("ep-box", EP_X, EP_Y, EP_W, EP_H, fill=C_ENDPOINT),
    text("ep-t", EP_X + 10, EP_Y + 8, EP_W - 20, 24,
         "FastAPI endpoints", size=14, bold=True, color="#c92a2a"),
    text("ep-b", EP_X + 10, EP_Y + 38, EP_W - 20, 240,
         "POST /ingest                  ← n8n W1 + W2\n"
         "POST /query                   ← Open WebUI\n"
         "        (reads LanceDB directly,\n"
         "         bypasses ingestion pipeline)\n"
         "GET  /sessions\n"
         "GET  /sessions/{session_id}\n"
         "GET  /speaker-aliases-block   ← n8n W2\n"
         "POST /reindex\n"
         "GET  /health\n"
         "auth: RETRIEVAL_API_KEY  (single key)",
         size=12),
]

# Storage column inside retrieval-server (right side)
STOR_X = 1700
STOR_W = 360
elements += [
    rect("stor-config", STOR_X, 350, STOR_W, 280, fill=C_VOLUME),
    text("stor-config-t", STOR_X + 10, 358, STOR_W - 20, 22,
         "config volume  (/app/config, rw)", size=14, bold=True, color="#a05a00"),
    text("stor-config-b", STOR_X + 10, 384, STOR_W - 20, 240,
         "speaker-aliases.yaml   (registry)\n"
         "entity-registry.yaml   (registry)\n"
         "extraction-config.yaml\n"
         "extraction-prompts/\n"
         "    chunk-extraction-vN.md\n"
         "    session-extraction-vN.md\n"
         "chunking.yaml          (token thresholds)\n"
         ".env                   (env_file overrides)",
         size=12),
]

# Pipeline panel (middle of retrieval-server, full width)
PIPE_X, PIPE_Y, PIPE_W, PIPE_H = 1300, 660, 760, 240
elements += [
    rect("pipe-box", PIPE_X, PIPE_Y, PIPE_W, PIPE_H, fill=C_ENDPOINT),
    text("pipe-t", PIPE_X + 10, PIPE_Y + 8, PIPE_W - 20, 24,
         "Ingestion pipeline  (community_brain.ingestion.pipeline)",
         size=14, bold=True, color="#c92a2a"),
    text("pipe-b", PIPE_X + 10, PIPE_Y + 40, PIPE_W - 20, 200,
         "1. Parser           — md artifacts → typed docs\n"
         "2. Chunker          — 3 strategies per content type\n"
         "3. Stage B          — session-level LLM extractor\n"
         "4. Stage C          — per-chunk LLM extractor\n"
         "5. Embedding        — Ollama nomic-embed-text\n"
         "6. Commit           — delete-then-add to LanceDB\n"
         "Idempotency anchor: extraction_prompt_version",
         size=12),
]

# LanceDB
elements += [
    rect("ldb-box", 1300, 920, 380, 100, fill=C_DB),
    text("ldb-t", 1310, 928, 360, 22,
         "LanceDB", size=14, bold=True),
    text("ldb-b", 1310, 952, 360, 70,
         "./community-brain/lancedb → /data/lancedb\n"
         "v1.0 schema · 37 fields · ground_truth |\n"
         "derived_metadata | provenance partitions",
         size=11),
]

# Output mount note (inside retrieval-server, right of LanceDB)
elements += [
    rect("out-mount", 1700, 920, 360, 100, fill=C_VOLUME),
    text("out-mount-t", 1710, 928, 340, 22,
         "shared output mount", size=14, bold=True, color="#a05a00"),
    text("out-mount-b", 1710, 952, 340, 70,
         "./output → /data/output  (READ-ONLY)\n"
         "constrained by\n"
         "COMMUNITY_BRAIN_ARTIFACT_ROOT",
         size=11),
]

# Networking note
elements += [
    rect("net-box", 1300, 1040, 760, 100, fill=C_DB),
    text("net-t", 1310, 1048, 740, 22,
         "Networking & deployment notes", size=14, bold=True),
    text("net-b", 1310, 1072, 740, 70,
         "extra_hosts: host.docker.internal → host-gateway  (Ollama on VM host)\n"
         "Port published 127.0.0.1:8999 only — NOT 0.0.0.0 (no LAN exposure)\n"
         "env_file: community-brain/config/.env  (operator overrides; required:false)",
         size=11),
]

# Trust contract note
elements += [
    rect("trust-box", 1300, 1160, 760, 100, fill="#f8f9fa"),
    text("trust-t", 1310, 1168, 740, 22,
         "Trust contract  (docs/inference-guidelines.md)",
         size=14, bold=True, color="#5f3dc4"),
    text("trust-b", 1310, 1192, 740, 70,
         "/query response is structurally partitioned. Quotes MUST resolve in\n"
         "ground_truth; derived_metadata is LLM-interpreted (probabilistic).\n"
         "Filter at openwebui/community_brain_filter.py enforces downstream.",
         size=11),
]

# =====================================================================
# ARROWS — orthogonal multi-segment, organized into lanes
# =====================================================================

# ----- LANE: External sources → n8n (left side, L-paths) -----
# A1: Mac Mini → ./watch  (rsync)
elements.append(arrow("a-mac-watch", [
    (360, 550), (390, 550), (390, 380), (440, 380),
], color="#0c8599", stroke_width=2))
elements.append(label("l-mac-watch", 245, 360,
                      "rsync (ssh)\nzoom-chat.txt", color="#0c8599"))

# A2: Fathom API → Fathom Poller  (poll)
elements.append(arrow("a-fathom-poller", [
    (360, 715), (400, 715), (400, 550), (440, 550),
], color="#0c8599", stroke_width=2))
elements.append(label("l-fathom-poller", 245, 690,
                      "poll every\n15 min", color="#0c8599"))

# ----- LANE: External AI services (top, vertical UP) -----
# A3: n8n container → OpenRouter  (n8n LLM aggregate)
# x=830 sits at the right edge of OpenRouter (range x=480..860) and is
# clear of both the VM title bbox (ends at x=420) and A4's overhead lane.
elements.append(arrow("a-n8n-or", [
    (830, 300), (830, 190),
], color="#5f3dc4", stroke_width=2, dashed=True))
elements.append(label("l-n8n-or", 670, 218,
                      "LLM × 8 (n8n workflows)", color="#5f3dc4"))

# A4: retrieval-server → OpenRouter  (Stage B/C LLM)
# Route OVER THE TOP — UP from retrieval at x=1750 to lane y=40 (above
# all AI service boxes which start at y=60), LEFT across to x=670, DOWN
# into OpenRouter top edge. This avoids crossing a-rs-ollama (vertical
# at x=1540, y=190..300).
elements.append(arrow("a-rs-or", [
    (1750, 300), (1750, 40), (670, 40), (670, 60),
], color="#5f3dc4", stroke_width=2, dashed=True))
elements.append(label("l-rs-or", 800, 18,
                      "LLM (Stage B/C extraction)  →  OpenRouter",
                      color="#5f3dc4"))

# A5: retrieval-server → Ollama  (embeddings)
elements.append(arrow("a-rs-ollama", [
    (1540, 300), (1540, 190),
], color="#0c8599", stroke_width=2, dashed=True))
elements.append(label("l-rs-ollama", 1555, 220,
                      "embed\n(nomic)", color="#0c8599"))

# A6: Open WebUI → retrieval-server  (POST /query)
# DOWN from Open WebUI bottom into retrieval-server top.
elements.append(arrow("a-owui-query", [
    (1960, 190), (1960, 300),
], color="#c92a2a", stroke_width=3))
elements.append(label("l-owui-query", 1820, 220,
                      "POST /query", color="#c92a2a"))

# Workflows write to ./output via filesystem — shown via the dashed
# border on the ./output box and the "n8n: rw / retrieval-server: ro"
# text inside it. Drawing additional arrows in the gap (x=1060..1100)
# would collide with A10's vertical at x=1080.

# ----- LANE: Workflows → /ingest  (over-the-top routing) -----
# Both ingest arrows enter the endpoints box from the LEFT side
# (avoids passing through the container title at the top). Lane y values
# 285 (A9) and 295 (A10) sit between VM-title bottom (y=280) and the
# container tops (y=300). Vertical "approach" lines at x=1289 (A9) and
# x=1285 (A10) keep them clear of each other AND of the title (now at x≥1660).
# A9: Merged Summarizer → POST /ingest
elements.append(arrow("a-merged-ingest", [
    (1060, 620), (1060, 285), (1289, 285), (1289, 395), (1300, 395),
], color="#c92a2a", stroke_width=3))

# A10: Transcript-Only → POST /ingest
elements.append(arrow("a-trans-ingest", [
    (1060, 820), (1080, 820), (1080, 295), (1285, 295), (1285, 405), (1300, 405),
], color="#c92a2a", stroke_width=3))

elements.append(label("l-ingest", 1100, 220,
                      "POST /ingest  (HTTP cross-container)",
                      color="#c92a2a"))

# ----- LANE: Shared output mount  (./output ↔ retrieval-server, dashed) -----
# A11: short horizontal at the output-mount note level
elements.append(arrow("a-out-mount", [
    (1260, 970), (1300, 970),
], color="#a05a00", stroke_width=2, dashed=True))
elements.append(label("l-out-mount", 1090, 940,
                      "shared mount\n(filesystem)", color="#a05a00"))

# ----- LANE: Internal retrieval-server (vertical, short) -----
# A12: /ingest endpoint → pipeline (aligned with A9 ingress at x=1500)
elements.append(arrow("a-ep-pipe", [
    (1500, 630), (1500, 660),
], color="#495057", stroke_width=2))

# A13: pipeline → LanceDB
elements.append(arrow("a-pipe-ldb", [
    (1500, 900), (1500, 920),
], color="#495057", stroke_width=2))

# /query → LanceDB: shown via label inside endpoints box (drawing this
# arrow would have to cut through the pipeline box). Logically /query
# bypasses the ingestion pipeline and reads LanceDB directly.

# ----- n8n_db connection (small internal vertical) -----
elements.append(arrow("a-n8n-db", [
    (750, 1110), (750, 1090),
], color="#495057", stroke_width=2, dashed=True))

# =====================================================================
# Legend (bottom of canvas)
# =====================================================================
LG_X, LG_Y = 40, 1480
elements += [
    rect("lg-box", LG_X, LG_Y, 2060, 80, fill="#ffffff", stroke="#868e96"),
    text("lg-t", LG_X + 15, LG_Y + 8, 400, 24, "Legend", size=14, bold=True),
    text("lg-b", LG_X + 15, LG_Y + 32, 2030, 60,
         "■ External services (yellow)   ■ n8n (blue)   ■ retrieval-server (green)   "
         "■ Volumes (orange)   ■ Databases (cyan)   ■ Endpoints (light red)   ■ Shared volume (amber)\n"
         "Solid red = HTTP API call across containers   Solid teal = network ingest (rsync, poll)   "
         "Solid orange = filesystem write   Dashed purple = LLM call   Dashed teal = embedding   "
         "Dashed amber = shared mount",
         size=11),
]

# =====================================================================
# Build the document
# =====================================================================
doc = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff",
        "gridSize": None,
    },
    "files": {},
}

OUT = "/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/docs/architecture.excalidraw"
with open(OUT, "w") as f:
    json.dump(doc, f, indent=2)

print(f"Wrote {OUT}  ({len(elements)} elements)")
