"""Tests for operations module."""

from src import operations

def test_add():
    """Test addition of positive and negative numbers."""
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0

