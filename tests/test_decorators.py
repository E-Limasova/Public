# tests/test_decorators.py

import os
import pytest
from decorators import log


def test_log_success(tmp_path):
    log_file = tmp_path / "success.log"

    @log(filename=log_file)
    def add(x, y):
        return x + y

    result = add(2, 3)

    assert result == 5
    with open(log_file) as f:
        contents = f.read()
        assert "add ok" in contents


def test_log_error(tmp_path):
    log_file = tmp_path / "error.log"

    @log(filename=log_file)
    def div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    with open(log_file) as f:
        contents = f.read()
        assert "div error: ZeroDivisionError" in contents
        assert "Inputs: (1, 0)" in contents


def test_log_console_success(capsys):
    @log()
    def mul(x, y):
        return x * y

    result = mul(3, 4)
    captured = capsys.readouterr()
    assert "mul ok" in captured.out


def test_log_console_error(capsys):
    @log()
    def sub(x, y):
        return x - y if x > y else 1 / 0

    with pytest.raises(ZeroDivisionError):
        sub(1, 2)

    captured = capsys.readouterr()
    assert "sub error: ZeroDivisionError" in captured.out
