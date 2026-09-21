"""Basic arithmetic operations for numeric values.

This module provides small, beginner-friendly functions for addition,
subtraction, multiplication, and division.
"""


def add(a, b):
    """Return the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The result of adding ``a`` and ``b``.
    """
    return a + b


def subtract(a, b):
    """Return the difference between two numbers.

    Args:
        a (int or float): The number from which to subtract.
        b (int or float): The number to subtract.

    Returns:
        int or float: The result of subtracting ``b`` from ``a``.
    """
    return a - b


def multiply(a, b):
    """Return the product of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The result of multiplying ``a`` and ``b``.
    """
    return a * b


def divide(a, b):
    """Return the quotient of two numbers.

    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        int or float: The result of dividing ``a`` by ``b``.

    Raises:
        ZeroDivisionError: If ``b`` is zero.
    """
    if b == 0:
        # Give the caller a clear error instead of attempting an invalid division.
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
