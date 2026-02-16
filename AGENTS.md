# Instructions

- Use Python best practice for 3.14 / 2026
- Add type-hints
- Fail fast
- Do not repeat your self
- Do not care about code formatting, ruff will handle this
- If running on Windows, use Power-Shell instead of bash for external commands
- After each code change run `uv run ruff format && uv run ruff check --fix --unsafe-fixes`
- After each new feature run `uv run pytest && uv run pre-commit run --all-files`
