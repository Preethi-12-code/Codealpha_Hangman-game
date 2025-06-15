# TASK 1: Hangman Game
import random

def hangman_game():
    # Predefined list of 5 words
    words = ["python", "computer", "programming", "software", "algorithm"]
    
    # Select a random word
    word_to_guess = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("🎮 Welcome to Hangman Game!")
    print(f"Guess the {len(word_to_guess)}-letter word")
    print("You have 6 incorrect guesses allowed\n")
    
    # Game loop
    while incorrect_guesses < max_incorrect:
        # Display current progress
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        
        # Check if word is completely guessed
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: {word_to_guess}")
            return
        
        # Get user input
        guess = input("\nEnter a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add guess to list
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in word_to_guess:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry! '{guess}' is not in the word.")
        
        print("-" * 40)
    
    # Game over
    print(f"\n💀 Game Over! You've run out of guesses.")
    print(f"The word was: {word_to_guess}")

def main():
    while True:
        hangman_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()