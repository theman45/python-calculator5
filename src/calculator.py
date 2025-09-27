"""Module defining Calculator class."""

from . import operations

class Calculator:
    """Simple calculator class wrapping arithmetic functions."""

    def add(self, a, b):
        """Return sum of two numbers using operations.add."""
        return operations.add(a, b)

    def subtract(self, a, b):
        """Return difference of two numbers using operations.subtract."""
        return operations.subtract(a, b)

    def multiply(self, a, b):
        """Return product of two numbers using operations.multiply."""
        return operations.multiply(a, b)

    def divide(self, a, b):
        """Return quotient of two numbers using operations.divide."""
        return operations.divide(a, b)
