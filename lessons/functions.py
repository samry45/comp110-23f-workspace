"""Learning functions."""


def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string."""
    return my_words


def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx."""
    if letter_idx < len(my_words):
        return str(my_words[letter_idx])
    else:
        return str("Index too high")