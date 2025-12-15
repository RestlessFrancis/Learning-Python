import random

print("Welcome to the Number Guessing Game!")

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

num = random.randint(low, high)

attempts = 5
chance_counter = 0

while chance_counter < attempts:
    chance_counter += 1
    guess =  int(input("Input your guess: "))


    if guess ==  num:
        print(f'Correct! The secret number is {num}. You guessed it in {chance_counter} attempts.')
        break

    elif chance_counter >= attempts and guess != num:
        print(f'Sorry, you have used all your attempts. The secret number was {num}.')

    elif guess < num:
        print("Your guess is too low!\n")
        
    elif guess > num:
        print("Your guess is too high!\n")

