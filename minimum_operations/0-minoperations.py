#!/usr/bin/python3
"""Minimum Operations: returns the fewest number of Copy All / Paste ops."""


def minOperations(n):
    """
    Calculate the minimum number of operations to get exactly n 'H' characters.

    Args:
        n (int): target number of H characters

    Returns:
        int: minimum operations, or 0 if impossible
    """
    if not isinstance(n, int) or n < 2:
        return 0

    ops = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1

    return ops
