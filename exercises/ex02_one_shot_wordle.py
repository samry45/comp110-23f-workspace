"""EX02 - One shot wordle!"""
__author__ = "730642818"

secret = str("python")
length_of_secret = int(len(secret))
guess = str(input(f"What is your {length_of_secret}-letter guess? "))
secret_letter = str(secret[0])
index = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
colors = str()
yellow_check = 0

# get correct length for guess
while len(secret) != len(guess):
    guess = str(input(f"That was not {length_of_secret} letters! Try again: "))
# check every letter to see if it matches
while index < len(secret):
    if (guess[index] == secret[index]):
        # if does match, add green box to string of emojis
        colors += (GREEN_BOX)
    else:
        # if doesn't match, check rest of word to see if it's anywhere
        second_index = 0
        while second_index < len(secret) and yellow_check != 1:
            if (guess[index] == secret[second_index]):
                yellow_check = 1
            second_index += 1
        if yellow_check == 1:
            colors += (YELLOW_BOX)
            yellow_check = 0
        else:
            colors += (WHITE_BOX)
    index += 1 
print(colors)
if secret == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")