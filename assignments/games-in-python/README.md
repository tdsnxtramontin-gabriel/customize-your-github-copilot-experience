# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game in Python. In this assignment, students will practice working with strings, loops, conditionals, random selection, and user input while creating an interactive terminal game.

## 📝 Tasks

### 🛠️ Create the Hangman game loop

#### Description
Create a Python program that selects a random word from a predefined list and lets the player guess one letter at a time. After each guess, display the current progress of the word using underscores for letters that have not been guessed yet.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Accept single-letter guesses from the user
- Display the current progress of the word in a format such as `_ _ _ _`
- Reveal correctly guessed letters in their proper positions
- Continue running until the word is fully guessed or the player runs out of attempts

### 🛠️ Track mistakes and show the game result

#### Description
Add logic to keep track of incorrect guesses and remaining attempts. At the end of the game, display a clear message telling the player whether they won or lost, and reveal the word if they did not guess it in time.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining
- Reduce the remaining attempts only when the player guesses a letter that is not in the word
- End the game with a win message when the player guesses the full word
- End the game with a lose message when the player uses all available attempts
- Show the hidden word at the end of the game if the player loses
