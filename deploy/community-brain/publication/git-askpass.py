#!/usr/bin/env python3
"""Git-only credential pipe: never invoke interactively or log its stdout."""

import os
import sys

if len(sys.argv) != 2:
    raise SystemExit(1)
prompt = sys.argv[1].lower()
if "username" in prompt:
    sys.stdout.write("x-access-token\n")
elif "password" in prompt:
    sys.stdout.write(os.environ["CB_PUBLISHER_GITHUB_TOKEN"] + "\n")
else:
    raise SystemExit(1)
