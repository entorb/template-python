#!/bin/sh

# exit upon error
set -e

# ensure we are in the root dir
cd "$(dirname "$0")/.."

# # update uv
# brew update && brew upgrade uv

uv python upgrade "$(cat .python-version)"

extract_from_toml() {
  uv run python -c "
import re, tomllib, sys
keys = sys.argv[1].split('.')
with open('pyproject.toml', 'rb') as f:
    data = tomllib.load(f)
for k in keys:
    data = data[k]
names = [re.split(r'[><=!~]+', d)[0].strip() for d in data]
print(' '.join(names))
" "$1"
}

DEPS=$(extract_from_toml "project.dependencies")
DEV_DEPS=$(extract_from_toml "dependency-groups.dev")

# Disables pathname expansion.
set -f

# remove all
[ -n "$DEPS" ] && uv remove $DEPS
[ -n "$DEV_DEPS" ] && uv remove --dev $DEV_DEPS

uv sync --upgrade

# Re-add at latest versions
[ -n "$DEPS" ] && uv add --upgrade $DEPS
[ -n "$DEV_DEPS" ] && uv add --upgrade --dev $DEV_DEPS

# Restore pathname expansion.
set +f

uv run ruff format
uv run ruff check --fix

uv run pre-commit autoupdate
uv run pre-commit run --all-files

echo DONE
