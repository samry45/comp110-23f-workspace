"""Combining two lists into a dictionary."""
__author__ = "730642818"


def zip(strings: list[str], numbers: list[int]) -> dict[str, int]:
    """Take two lists and put them together in one dictionary."""
    together: dict[str, int] = {}
    if len(strings) != len(numbers):
        return together
    idx = 0
    while idx < len(numbers):
        together[strings[idx]] = numbers[idx]
        idx += 1
    return together
