import pytest
import sys
from typing import TypeVar, Callable, Any, cast
from loguru import logger
from src.decorators import log


def test_my_function_valid(capsys) -> None:
    logger.remove()
    logger.add(sys.stdout)

    _ = capsys.readouterr()

    @log()
    def my_function(x: int, y: int) -> float:
        return x / y

    result1 = my_function(100, 50)
    assert result1 == 2.0

    captured = capsys.readouterr()
    assert "my_function | ok" in captured.out


def test_my_function_raise(capsys) -> None:
    logger.remove()
    logger.add(sys.stdout)

    _ = capsys.readouterr()

    @log()
    def my_function(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(100, 0)
    captured = capsys.readouterr()
    assert "my_function error: | ZeroDivisionError" in captured.out
