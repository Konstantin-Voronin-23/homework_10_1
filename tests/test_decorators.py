import sys

import pytest
from loguru import logger

from src.decorators import log


def test_my_function_valid(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет корректность стандартных операций"""
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


def test_my_function_invalid(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет корректность нестандартных операций в данном примере с отрицательными значениями"""
    logger.remove()
    logger.add(sys.stdout)

    _ = capsys.readouterr()

    @log()
    def my_function(x: int, y: int) -> float:
        return x / y

    result1 = my_function(-1000, 50)
    assert result1 == -20.0

    captured = capsys.readouterr()
    assert "my_function | ok" in captured.out


def test_my_function_raise(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет корректную отработку исключений в данном примере при делении на 0"""
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
