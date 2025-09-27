"""Tests for Calculator class."""

import pytest

from src.calculator import Calculator

calc = Calculator()

def test_add():
    """Test addition using Calculator."""
    assert calc.add(2, 3) == 5

def test_subtract():
    """Test subtraction using Calculator."""
    assert calc.subtract(10, 4) == 6

def test_multiply():
    """Test multiplication using Calculator."""
    assert calc.multiply(3, 3) == 9

def test_divide():
    """Test division using Calculator."""
    assert calc.divide(8, 2) == 4

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        calc.divide(4, 0)
