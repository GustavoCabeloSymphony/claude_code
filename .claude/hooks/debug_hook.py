#!/usr/bin/env python3
"""
Debug hook to see what input Claude Code is passing.
"""
import json
import sys
from datetime import datetime

# Log the input to a debug file
debug_file = "/Users/gcabelo/Symphony/Projects/claude_code/.claude/hooks/debug.log"

try:
    input_data = sys.stdin.read()

    with open(debug_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Raw input:\n{input_data}\n")

        try:
            parsed = json.loads(input_data)
            f.write(f"\nParsed JSON:\n{json.dumps(parsed, indent=2)}\n")
        except Exception as e:
            f.write(f"\nJSON parse error: {e}\n")

    print("Debug hook executed successfully", file=sys.stderr)

except Exception as e:
    with open(debug_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"ERROR: {e}\n")
    sys.exit(1)
