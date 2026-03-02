#!/usr/bin/env python3
"""Validate that all JSON files under the schema directory are well-formed."""

import json
import sys
from pathlib import Path


def validate_json_files(schema_dir: str) -> int:
    """Validate every *.json file found under schema_dir.

    Returns 0 if all files are valid, 1 if any file is invalid.
    """
    has_error = False
    json_files = sorted(Path(schema_dir).rglob("*.json"))

    if not json_files:
        print(f"No JSON files found under '{schema_dir}'.")
        return 0

    for filepath in json_files:
        try:
            with open(filepath, encoding="utf-8") as f:
                json.load(f)
            print(f"VALID: {filepath}")
        except json.JSONDecodeError as exc:
            print(f"INVALID: {filepath} — {exc}", file=sys.stderr)
            has_error = True

    return 1 if has_error else 0


if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "schema"
    sys.exit(validate_json_files(directory))
