"""
Example Python script.
"""

import datetime as dt
import logging
from pathlib import Path
from zoneinfo import ZoneInfo

import tomli_w

from helper_logging import init_logging

init_logging()
LOGGER = logging.getLogger(__name__)

TZ_DE = ZoneInfo("Europe/Berlin")


def calc_sum(x: int, y: float) -> float:
    """Calculate the sum of an integer and a float."""
    return x + y


def read_file(filename: Path) -> str:
    """Read a file and return first line."""
    with filename.open(encoding="utf-8") as f:
        return f.readline().strip()


def get_date() -> dt.date:
    """Return the current date."""
    return dt.datetime.now(tz=TZ_DE).date()


def write_toml_file(path: Path, config: dict) -> None:
    """Export a dict as a .toml. file."""
    with path.open("wb") as fh:
        tomli_w.dump(config, fh)


def main() -> None:  # noqa: D103 pragma: no cover
    print(calc_sum(1, 2.2))
    print(read_file(Path("LICENSE")))
    print(get_date())
    p = Path("test.toml")
    write_toml_file(path=p, config={"var1": 123.3, "var2": "str"})
    p.unlink()


if __name__ == "__main__":
    main()
