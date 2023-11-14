""""Dictionaries Functions - EX06!"""
__author__ = "730642818"


def invert (flip: dict[str, str]) -> dict[str, str]:
    """Invert all the key/value pairs."""
    flipped: dict[str, str] = {}
    for key in flip:
        flipped[flip[key]] = key
    return flipped
    # If you encounter more than one of the same key when trying to invert your dictionary, raise a KeyError.

def favorite_color (colors: dict[str, str]) -> str:
    """Return the most common favorite color."""
    popular: str = colors["Marc"]
    return popular

#define first color as best
#make count varibale to keep track of counts
#highest count wins