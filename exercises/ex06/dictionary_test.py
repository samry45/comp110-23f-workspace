"""Testing dictionary functions."""
__author__ = "730642818"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_invert_empty_input() -> None:
    """Function invert should return an empty dict if an empty dict is inputted."""
    assert invert({}) == {}


def test_invert_dict_length_2() -> None:
    """Function invert should return the dict with the key and value reversed."""
    input_dict: dict[str, str] = {"Samantha": "Holtgrewe", "Meredith": "Benton"}
    assert invert(input_dict) == {"Holtgrewe": "Samantha", "Benton": "Meredith"}


def test_invert_dict_length_3() -> None:
    """Function invert should return the dict with the key and value reversed."""
    input_dict: dict[str, str] = {"Samantha": "Rylee", "Alexander": "Davis", "Andrew": "Ray"}
    assert invert(input_dict) == {"Rylee": "Samantha", "Davis": "Alexander", "Ray": "Andrew"}


def test_favorite_color_empty_input() -> None:
    """Function favorite_color should return an empty str if an empty dict is inputted."""
    assert favorite_color({}) == ""


def test_favorite_color_simple() -> None:
    """Function favorite_color should return the most common color in the dict."""
    input_dict: dict[str, str] = {"Samantha": "blue", "Ainsley": "yellow", "Alex": "blue"}
    assert favorite_color(input_dict) == "blue"


def test_favorite_color_complex() -> None:
    """Function favorite_color should return the most common color in the dict."""
    input_dict: dict[str, str] = {"Samantha": "blue", "Ainsley": "yellow", "Alex": "blue", "Steven": "blue", "Amelia": "yellow"}
    assert favorite_color(input_dict) == "blue"


def test_favorite_color_tie() -> None:
    """Function favorite_color should return the first color if tied."""
    input_dict: dict[str, str] = {"Samantha": "blue", "Ainsley": "yellow", "Alex": "blue", "Amelia": "yellow"}
    assert favorite_color(input_dict) == "blue"


def test_count_empty_input() -> None:
    """Function count should return an empty dict if an empty list is inputted."""
    assert count([]) == {}


def test_count_simple() -> None:
    """Function count should return a dict with each word and its frequency count."""
    input_dict: dict[str, str] = ["apple", "apple", "orange", "banana", "orange"]
    assert count(input_dict) == {"apple": 2, "orange": 2, "banana": 1}


def test_count_one_word() -> None:
    """Function count should return a dict with one key/value pair."""
    input_dict: dict[str, str] = ["Samantha", "Samantha", "Samantha", "Samantha", "Samantha", "Samantha", "Samantha", "Samantha"]
    assert count(input_dict) == {"Samantha": 8}


def test_alphabetizer_empty_input() -> None:
    """Function alphabetizer should return an empty dict."""
    assert alphabetizer([]) == {}


def test_alphabetizer_lowercase() -> None:
    """Function alphabetizer should return a dict with the words sorted by letter."""
    input_list: list[str] = ["chair", "table", "couch", "stairs", "wall", "window"]
    assert alphabetizer(input_list) == {"c": ["chair", "couch"], "t": ["table"], "s": ["stairs"], "w": ["wall", "window"]}


def test_alphabetizer_uppercase() -> None:
    """Function alphabetizer should return a dict with the words sorted by letter."""
    input_list: list[str] = ["Samantha", "stairs", "couch", "table", "Conner", "Meredith"]
    assert alphabetizer(input_list) == {"s": ["Samantha", "stairs"], "c": ["couch", "Conner"], "t": ["table"], "m": ["Meredith"]}


def test_update_attendance_missing_input() -> None:
    """Function update_attendance should return the same dict as the input."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Samantha", "Meredith"], "Tuesday": ["Aidan", "Meredith"], "Wednesday": ["Samantha"]}
    assert update_attendance(attendance_log, "", "") == {"Monday": ["Samantha", "Meredith"], "Tuesday": ["Aidan", "Meredith"], "Wednesday": ["Samantha"]}


def test_update_attendance_once() -> None:
    """Function attendance should be updated to add the person to the day list."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Samantha", "Meredith"], "Tuesday": ["Aidan", "Meredith"], "Wednesday": ["Samantha"]}
    input_day: str = "Monday"
    input_person: str = "Aidan"
    assert update_attendance(attendance_log, input_day, input_person) == {"Monday": ["Samantha", "Meredith", "Aidan"], "Tuesday": ["Aidan", "Meredith"], "Wednesday": ["Samantha"]}


def test_update_attendance_add_day() -> None:
    """Function attendance log should add another key/value pair with a new day."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Samantha", "Meredith"], "Tuesday": ["Aidan", "Meredith"], "Wednesday": ["Samantha"]}
    input_day: str = "Thursday"
    input_person: str = "Meredith"
    assert update_attendance(attendance_log, input_day, input_person) == {"Monday": ["Samantha", "Meredith"], "Tuesday": ["Aidan", "Meredith"], "Wednesday": ["Samantha"], "Thursday": ["Meredith"]}
