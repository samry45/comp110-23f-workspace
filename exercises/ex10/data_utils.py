"""Dictionary related utility functions."""

__author__ = "730642818"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of values under specific header."""
    result: list[str] = []
    for elem in table:
        result.append(elem[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictioanry with column headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result

def head(data: dict[str, list[str]], length: int) -> dict[str, list[str]]:
    """Return only the first few lines of the dataset."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = data[0]
    for key in first_row:
        values: list[str] = []
        for x in range length:
            values.append(data[x])
        result[key] = values
    return result