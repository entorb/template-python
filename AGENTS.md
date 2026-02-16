# Instructions

- Use Python best practice for 3.14 / 2026
- All functions/methods MUST have type annotations including return types, use modern type hints: `list[str]`, `dict[str, int]` (not `List`, `Dict` from typing)
- Fail fast
- Doc strings: Short Google style with Args/Returns/Raises sections
- Do not repeat your self
- Do not care about code formatting, ruff will handle this
- Use f-strings for formatting, avoid `.format()` or `%`
- If running on Windows, use Power-Shell instead of bash for external commands
- After each code change run `uv run ruff format && uv run ruff check --fix --unsafe-fixes`
- After each new feature run `uv run pytest && uv run pre-commit run --all-files`
