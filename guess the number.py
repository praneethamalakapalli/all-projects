import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = 0

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print(f"Congratulations! You guessed the number in {attempts} attempts.")

guess_the_number()
