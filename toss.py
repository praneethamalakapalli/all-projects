import random

def hangman():
    words = ['praneetha','dhanush','gayatri','ashritha']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Let's play Hangman!")
    
    while attempts > 0 and ''.join(guessed_word) != word:
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess!")
    
    if ''.join(guessed_word) == word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

hangman()


