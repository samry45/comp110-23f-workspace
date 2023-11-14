"""Testing my sum of evens function."""

from lessons.sum_evens import sum_evens_of_list


def test_empty_list() -> None:
    """sum_evens_of_list([]) should return 0."""
    assert sum_evens_of_list([]) == 0


def test_sum_one_element() -> None:
    """sum_evens_of_list([2]) should return 2."""
    test_list: list[int] = [2]
    assert sum_evens_of_list(test_list) == 2


def test_sum_positives() -> None:
    """sum_evens_of_list([positives]) should work."""
    test_list: list[int] = [1, 2, 3, 4]
    assert sum_evens_of_list(test_list) == 6


def test_sum_neg_and_positives() -> None:
    """sum_evens_of_list with negatives and positives should still work."""
    test_list: list[int] = [-1, -2, 3, 4]
    assert sum_evens_of_list(test_list) == 2


def test_sum_odd_numbers() -> None:
    """sum_evens_of_list with odd numbers should return 0."""
    test_list: list[int] = [1, 3, 5, 7]
    assert sum_evens_of_list(test_list) == 0