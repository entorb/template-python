"""Unit Tests for example.py."""

# ruff: noqa: S101 D103 PLR2004 INP001

import sys
from pathlib import Path

sys.path.insert(0, (Path(__file__).parent.parent / "src").as_posix())

import datetime as dt

from example import calc_sum, get_date, read_file


def test_calc_sum() -> None:
    assert calc_sum(1, 2) == 3


def test_read_file() -> None:
    assert read_file(Path("LICENSE")) == "GNU GENERAL PUBLIC LICENSE"


def test_get_date() -> None:
    assert get_date() >= dt.date(2023, 3, 14)
