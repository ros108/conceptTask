import random
words = ["apple", "orange", "mango"]
original_word = random.choice(words)
scrambled_word = "".join(random.sample(original_word, len(original_word)))

attempts = 5

print("Welcome to the Word Scramble Game!")
print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
while attempts > 0:
    guess = input("Enter your guess: ").strip() 
    if guess == original_word:
        print("Congratulations! You guessed the correct word!")
        break
    else:
        attempts -= 1  
        if attempts > 0:
            print(f"Incorrect! Try again. You have {attempts} attempts left.")
        else:
            print(f"You're out of attempts! The correct word was: {original_word}")