"""Unit Tests for example.py."""

import datetime as dt
import tomllib
from pathlib import Path

import pytest

from main import calc_sum, get_date, read_file, write_toml_file


@pytest.mark.parametrize(("x", "y", "expected"), [(1, 1, 2), (1, 2, 3), (1, 0, 1)])
def test_task_est_to_minutes(x: int, y: int, expected: int) -> None:
    assert calc_sum(x, y) == expected


def test_read_file() -> None:
    assert read_file(Path("LICENSE")) == "GNU GENERAL PUBLIC LICENSE"


def test_get_date() -> None:
    assert get_date() >= dt.date(2023, 3, 14)


def test_write_toml_file() -> None:
    p = Path("test.toml")
    c = {"var1": 123, "var2": "str"}
    p.unlink(missing_ok=True)
    assert not p.is_file(), f"File {p} should not exists"
    write_toml_file(path=p, config=c)
    assert p.is_file(), f"File {p} should exists"

    with p.open("rb") as fh:
        o = tomllib.load(fh)  # type: ignore
        assert o["var1"] == 123
        assert o["var2"] == "str"

    p.unlink()
    assert not p.is_file(), f"File {p} should not exists"
