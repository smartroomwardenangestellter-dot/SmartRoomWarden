#!/usr/bin/env bash
# Run project unit tests (POSIX)
set -euo pipefail

VENV_PY=${VENV_PY:-.venv/Scripts/python.exe}
if [ -x "$VENV_PY" ]; then
  "$VENV_PY" -m unittest discover -s tests -p 'test_*.py' -v
else
  python -m unittest discover -s tests -p 'test_*.py' -v
fi

echo "Tests completed."
