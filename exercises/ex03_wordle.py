"""Structured Wordle!"""
__author__ = "730642818"


def contains_char(secret_word: str, letter_guess: str) -> bool:
    """If the letter is found anywhere in the word, return True."""
    assert len(letter_guess) == 1
    index = 0
    while len(secret_word) > index:
        if secret_word[index] == letter_guess:
            return True
        index += 1
    return False


def emojified(word_guess: str, secret_word: str) -> str:
    """Produce colored boxes for each letter if they are in the word and/or in the right spot."""
    assert len(word_guess) == len(secret_word)
    index = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    colors = str()
    while len(word_guess) > index:
        if word_guess[index] == secret_word[index]:
            colors += GREEN_BOX
        elif contains_char(secret_word, word_guess[index]):
            colors += YELLOW_BOX
        else:
            colors += WHITE_BOX
        index += 1
    return colors


def input_guess(characters: int) -> str:
    """Ask for a word guess and check length."""
    word_guess = str(input("Enter a " + str(characters) + " character word: "))
    while len(word_guess) != characters:
        word_guess = str(input("That wasn't " + str(characters) + " chars! Try again: "))
    return word_guess


def main() -> None:
    """Run full wordle game!"""
    turn = 1
    secret_word = str("codes")
    word_guess = str()
    while turn <= 6 and word_guess != secret_word:
        print("=== Turn " + str(turn) + "/6 ===")
        word_guess = input_guess(len(secret_word))
        print(emojified(word_guess, secret_word))
        turn += 1
    if word_guess == secret_word:
        print("You won in " + str(turn - 1) + "/6 turns!")
    else:  # word_guess != secret_word
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()