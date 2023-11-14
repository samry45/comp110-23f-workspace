"""Program that loops until correct number is guessed."""

from random import randint

secret: int = randint(1, 100)
guess: int = int(input("Guess a number between 1 and 100: "))
number_of_tries: int = 1
max_tries: int = 10

while guess != secret and number_of_tries < max_tries:
    print("Wrong!")
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    guess = int(input("Guess again: "))
    number_of_tries += 1
if guess == secret:
    print("Congrats! You guessed correctly in " + str(number_of_tries) + " tries!")
else:
    print("You lose! :(")