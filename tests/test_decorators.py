import sys

import pytest
from loguru import logger

from src.decorators import log, number_divide


def test_log_valid(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет корректность стандартных операций"""

    logger.add(sys.stdout)
    _ = capsys.readouterr()

    @log()
    def number_divide(x: int, y: int) -> float:
        return x / y

    result1 = number_divide(100, 50)
    assert result1 == 2.0

    captured = capsys.readouterr()
    assert "number_divide | ok" in captured.out


def test_log_invalid(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет корректность нестандартных операций в данном примере с отрицательными значениями"""

    logger.add(sys.stdout)
    _ = capsys.readouterr()

    @log()
    def number_divide(x: int, y: int) -> float:
        return x / y

    result1 = number_divide(-1000, 50)
    assert result1 == -20.0

    captured = capsys.readouterr()
    assert "number_divide | ok" in captured.out


def test_log_raise(capsys: pytest.CaptureFixture) -> None:
    """Тест проверяет корректную отработку исключений в данном примере при делении на 0"""

    logger.add(sys.stdout)
    _ = capsys.readouterr()

    @log()
    def number_divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        number_divide(100, 0)
    captured = capsys.readouterr()
    assert "number_divide error: | ZeroDivisionError" in captured.out


def test_number_divide_valid() -> None:
    """Тест для проверки положительных чисел"""
    assert number_divide(2, 1) == 2.0


def test_number_divide_invalid() -> None:
    """Тест для проверки отрицательных чисел"""
    assert number_divide(-500, 20) == -25.0


def test_number_divide_raise() -> None:
    """Тест для проверки исключений функции"""
    with pytest.raises(ZeroDivisionError):
        number_divide(359, 0)
