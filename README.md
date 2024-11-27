# main Function
## Description
The main function calculates various statistics based on the daily step counts for a month. The user provides the step counts as input, and the function computes the following insights:

The highest step count in the month.
The lowest step count in the month.
The average step count for the month.
A sorted list of step counts in descending order.
Features
User Input: Accepts daily step counts for a month as a single input string.
Data Processing:
Converts the input into a list of integers.
Calculates statistics such as the highest, lowest, and average step counts.
Sorts step counts in descending order.
Output: Displays the results in a clear and user-friendly format.

ex:
Input
```
Enter the number of steps taken each day in the month (separated by spaces): 5000 7500 8200 6000 9500 12000 4500 4800 5600 8000
```
[problem 1](https://drive.google.com/file/d/1NhJz4bc433y8ykJd6pcWk236JzLqwVVU/view?usp=drive_link) 

# library_analysis Function
## Description
The library_analysis function is designed to process a list of library borrowing records, analyze the data, and provide insights such as the most and least borrowed books, average borrowing duration, unique book titles, and a sorted list of books based on borrowing duration.

Features
Data Processing: Aggregates the total borrowing days for each book from a list of records.
Insights:
Identifies the most and least borrowed books.
Calculates the average borrowing duration across all books.
Lists unique book titles.
Sorts books by borrowing duration in descending order.
Display Results: Outputs all insights in a user-friendly format.
ex:

Input
```
records = [
    "Harry Potter - 12",
    "The Hobbit - 8",
    "Harry Potter - 5",
    "1984 - 15",
    "The Catcher in the Rye - 6",
    "The Hobbit - 7"
]
```

[problem 2](https://drive.google.com/file/d/1VZyT99igTwKgbG2wf4SMPqSlRhJyf0Us/view?usp=drive_link) 
# Word Scramble Game README
## Overview
The Word Scramble Game is a simple Python program that allows users to guess the original word from a scrambled version. It provides players with a fun and interactive way to practice problem-solving and guessing skills.

Features
Random Word Selection: A random word is selected from a predefined list.
Scrambling: The word's letters are shuffled in a random order.
Multiple Attempts: Players have up to 5 attempts to guess the word.
Dynamic Feedback: Players are informed whether their guess is correct or incorrect, and how many attempts remain.
Graceful Error Handling: Handles invalid or empty input effectively.

Example Interaction
```
Welcome to the Word Scramble Game!
Try to guess the original word from the scrambled word: pleap
You have 5 attempts.

Enter your guess: leap
Incorrect! Try again. You have 4 attempts left.

Enter your guess: apple
Congratulations! You guessed the correct word!
```
