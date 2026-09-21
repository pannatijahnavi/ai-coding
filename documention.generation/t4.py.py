"""Simple conversions between decimal, binary, and hexadecimal numbers.

The conversion functions in this module work with non-negative decimal
integers and binary strings containing only 0 and 1.
"""


def decimal_to_binary(n):
    """Convert a non-negative decimal integer to a binary string.

    Args:
        n (int): The non-negative decimal integer to convert.

    Returns:
        str: The binary representation of ``n`` without a ``0b`` prefix.

    Raises:
        ValueError: If ``n`` is negative.
        TypeError: If ``n`` is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return bin(n)[2:]


def binary_to_decimal(b):
    """Convert a binary string to a decimal integer.

    Args:
        b (str): A non-empty string containing only ``0`` and ``1``.

    Returns:
        int: The decimal value represented by ``b``.

    Raises:
        TypeError: If ``b`` is not a string.
        ValueError: If ``b`` is empty or contains a character other than
            ``0`` or ``1``.
    """
    if not isinstance(b, str):
        raise TypeError("b must be a string.")
    if not b or any(digit not in "01" for digit in b):
        raise ValueError("b must be a non-empty binary string.")
    return int(b, 2)


def decimal_to_hexadecimal(n):
    """Convert a non-negative decimal integer to a hexadecimal string.

    Args:
        n (int): The non-negative decimal integer to convert.

    Returns:
        str: The hexadecimal representation of ``n`` with a ``0x`` prefix.

    Raises:
        ValueError: If ``n`` is negative.
        TypeError: If ``n`` is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return hex(n)
