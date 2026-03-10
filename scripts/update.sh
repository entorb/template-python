#!/bin/sh

# ensure we are in the root dir
cd "$(dirname "$0")"/..

# exit upon error
set -e

# to update uv on macos:
# brew update && brew upgrade uv

uv python upgrade

# upgrade all dependencies remove & re-add needed, as otherwise uv does not update pyproject.toml

uv remove python-dotenv tzdata
uv remove --dev pre-commit pytest pytest-cov ruff

uv lock --upgrade
uv sync --upgrade

uv add --upgrade python-dotenv tzdata
uv add --upgrade --dev pre-commit pytest pytest-cov ruff

# ruff
uv run ruff check --fix
uv run ruff format

# pre-commit
uv run pre-commit autoupdate
uv run pre-commit run --all-files

echo DONE
