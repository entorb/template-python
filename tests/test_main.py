"""Unit Tests for example.py."""

import datetime as dt
from pathlib import Path

import pytest

from main import calc_sum, get_date, read_file


@pytest.mark.parametrize(("x", "y", "expected"), [(1, 1, 2), (1, 2, 3), (1, 0, 1)])
def test_calc_sum(x: int, y: float, expected: float) -> None:
    assert calc_sum(x, y) == expected


def test_read_file() -> None:
    assert read_file(Path("LICENSE")) == "GNU GENERAL PUBLIC LICENSE"


def test_get_date() -> None:
    assert get_date() >= dt.date(2023, 3, 14)
