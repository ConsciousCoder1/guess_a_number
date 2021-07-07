import random

# Welcome user and obtain user name and number guess

print("Hello! Welcome to the Guess a Number game. You'll have to guess my secret number. Good luck!")
user_name = input("What is your name? ")
random_number = random.randint(1, 20)
print(f"Well, {user_name}, I'm thinking of a number between 1 and 20.")

# Prompt user for number guesses

for user_tries in range(1, 7):
    print("Enter a guess: ")
    user_guess = int(input())
    if user_guess < random_number:
        print("Your guess is too low.")
    elif user_guess > random_number:
        print("Your guess is too high.")
    else: 
        break
    
# User won or lost

if user_guess == random_number:
    print(f"Congratulations, {user_name}! You guessed my number in {user_tries} tries.")
else:
    print(f"Actually, the number I was thinking of was {random_number}.")