"""
Example Python script.
"""

import datetime as dt
from pathlib import Path
from zoneinfo import ZoneInfo

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


if __name__ == "__main__":
    print(calc_sum(1, 2.2))
    print(read_file(Path("LICENSE")))
    print(get_date())
