"""Test my zip function."""
__author__ = "730642818"

from lessons.zip import zip


def test_two_empty_list() -> None:
    """Function zip with empty lists should return an empty dict."""
    test_strings: list[str] = []
    test_numbers: list[int] = []
    assert zip(test_strings, test_numbers) == {}


def test_two_3_item_lists() -> None:
    """Function zip should take two lists and put them together in one dictioanry."""
    test_strings: list[str] = ["Happy", "Halloween", "Everyone"]
    test_numbers: list[int] = [1, 2, 3]
    assert zip(test_strings, test_numbers) == {"Happy": 1, "Halloween": 2, "Everyone": 3}


def test_two_2_item_lists() -> None:
    """Function zip should take two lists and put them together in one dictionary."""
    test_strings: list[str] = ["Happy", "Halloween"]
    test_numbers: list[int] = [1, 2]
    assert zip(test_strings, test_numbers) == {"Happy": 1, "Halloween": 2}


def test_two_different_sized_lists() -> None:
    """Function zip should return an empty dictionary if the lists are different lengths."""
    test_strings: list[str] = ["Happy", "Halloween"]
    test_numbers: list[int] = [1, 2, 3]
    assert zip(test_strings, test_numbers) == {}