#!/bin/sh

set -e
cd "$(dirname "$0")"/..

# # update uv
# brew update
# brew upgrade uv

uv python upgrade

extract_from_toml() {
  uv run python3 -c "
import re, tomllib, sys
keys = sys.argv[1].split('.')
with open('pyproject.toml', 'rb') as f:
    data = tomllib.load(f)
try:
    for k in keys:
        data = data[k]
except KeyError:
    data = []
names = [re.split(r'[><=!~]+', d)[0].strip() for d in data]
print(' '.join(names))
" "$1"
}

DEPS=$(extract_from_toml "project.dependencies")
DEV_DEPS=$(extract_from_toml "dependency-groups.dev")

# Remove all deps so uv re-adds at latest versions
[ -n "$DEPS" ] && uv remove $DEPS
[ -n "$DEV_DEPS" ] && uv remove --dev $DEV_DEPS

uv lock --upgrade
uv sync --upgrade

# Re-add at latest versions
[ -n "$DEPS" ] && uv add --upgrade $DEPS
[ -n "$DEV_DEPS" ] && uv add --upgrade --dev $DEV_DEPS

uv run ruff format
uv run ruff check --fix

uv run pre-commit autoupdate
uv run pre-commit run --all-files

echo DONE
