"""Tests for operations module."""
import pytest

from src import operations


def test_add():
    """Test addition of positive and negative numbers."""
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0

def test_subtract():
    """Test subtraction of numbers."""
    assert operations.subtract(5, 3) == 2

def test_multiply():
    """Test multiplication of numbers."""
    assert operations.multiply(2, 4) == 8

def test_divide():
    """Test division of numbers."""
    assert operations.divide(10, 2) == 5

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    
    with pytest.raises(ValueError):
        operations.divide(5, 0)
