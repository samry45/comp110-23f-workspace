"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730642818"

word_guess = str(input("Enter a 5-character word: "))
if len(word_guess) != 5:
     print ("Error: Word must contain 5 characters")
     exit()
character_guess = str(input("Enter a single character: "))
if len(character_guess) != 1:
     print ("Error: Character must be a single character")
     exit()
number_characters = int(0)

print ("Searching for " + character_guess + " in " + word_guess)
if str(word_guess)[0] == str(character_guess):
    number_characters = number_characters + 1
    print (character_guess + " found at index 1")
if str(word_guess)[1] == str(character_guess):
    number_characters = number_characters + 1
    print (character_guess + " found at index 2")
if str(word_guess)[2] == str(character_guess):
    number_characters = number_characters + 1
    print (character_guess + " found at index 3")
if str(word_guess)[3] == str(character_guess):
    number_characters = number_characters + 1
    print (character_guess + " found at index 4")
if str(word_guess)[4] == str(character_guess):
    number_characters = number_characters + 1
    print (character_guess + " found at index 5")

if number_characters == 0:
     print ("No instances of " + str(character_guess) + " found in " + str(word_guess))
if number_characters == 1:
    print (str(number_characters) + " instance of " + str(character_guess) + " found in " + str(word_guess))
if number_characters > 1:
        print (str(number_characters) + " intances of " + str(character_guess) + " found in " + str(word_guess))