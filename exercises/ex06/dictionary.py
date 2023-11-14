"""Dictionary practice with functions."""
__author__ = "730642818"


def invert(flip: dict[str, str]) -> dict[str, str]:
    """Invert all the key/value pairs."""
    flipped: dict[str, str] = {}
    for key in flip:
        flipped[flip[key]] = key
    if len(flipped) != len(flip):
        raise KeyError("Error! Duplicate key found.")
    return flipped


def favorite_color(colors: dict[str, str]) -> str:
    """Return the most common favorite color."""
    color_counter: dict[str, int] = {}
    winning: str = ""
    for key in colors:
        color = colors[key]
        if color in color_counter:
            color_counter[color] += 1
        else:
            color_counter[color] = 1
    highest_number: int = 0
    for key in color_counter:
        if color_counter[key] > highest_number:
            highest_number += 1
            winning = key
    return winning


def count(words: list[str]) -> dict[str, int]:
    """Count the frequency of each item on the list."""
    counter: dict[str, int] = {}
    for item in words:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Sort the words by starting letter."""
    sorted: dict[str, list[str]] = {}
    for item in words:
        sorted_words: list[str] = []
        sorted_words.append(item)
        letter: str = item[0]
        low_letter = letter.lower()
        if low_letter in sorted:
            sorted[low_letter] += sorted_words
        else: 
            sorted[low_letter] = sorted_words
    return sorted


def update_attendance(attendance: dict[str, list[str]], day: str, person: str) -> dict[str, list[str]]:
    """List the people who were present for each day."""
    people: list[str] = []
    attendance_updated: dict[str, list[str]] = {}
    for key in attendance:
        people = attendance[key]
        attendance_updated[key] = attendance[key]
        if day in attendance and person not in attendance:
            people.append(person)
            attendance_updated[day] = people
        else:
            new_people: list[str] = [person]
            attendance_updated[day] = new_people
    return attendance_updated


attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)