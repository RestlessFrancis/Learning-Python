import random

name = input("Enter your name: ")

print("Goodluck!", name)

word = [
    'python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'developer', 'function', 'variable', 'condition'
]

word = random.choice(word)

print("Guess the characters")

guesses = ''
turns = 5

while turns > 0:
    failed = 0

    for char in word:
        
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win!")
        print("The word is: ", word)
        break

    print()
    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print(f'You have {turns} more guesses')

        if turns == 0:
            print("You lose")