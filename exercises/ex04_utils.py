"""Practicing Utility Functions."""
__author__ = "730642818"


def all(numbers: list[int], guess: int) -> bool:
    """Produce True if list is comprised of only the guessed integer."""
    test_idx = 0
    test_result = 0
    if len(numbers) == 0:
        return False
    while test_idx < len(numbers) and test_result == 0:
        if numbers[test_idx] == guess:
            test_result = 0
        else:
            test_result = 1
        test_idx += 1
    if test_result == 0:
        return True
    else:
        return False


def max(numbers: list[int]) -> int:
    """Return largest number in list."""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    high_num = numbers[0]
    test_idx = 0
    while test_idx < len(numbers):
        if numbers[test_idx] > high_num:
            high_num = numbers[test_idx]
        test_idx += 1
    return high_num


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Produce True if lists are identical."""
    if input1 == input2:
        return True
    else:
        return False