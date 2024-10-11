# Project : Number Guessing Game
### ► Audience : Beginners 👶
### ► Difficulty : Easy ◉○○○
### ► Required Packages : None

---
#### Tasks:
* Build a number guessing game, in which the user selects a range.
* Let’s say user selected a range, i.e., from A to B, where A and B belong to integer.
* Some random integer will be selected by the system and the user has to guess that integer.
* Print total number of guesses to the console.

#### Explanation: 

If the user inputs range, let’s say from 1 to 100. And compiler randomly selected 42 as the integer. And now the guessing game started, so the user entered 50 as his/her first guess. The compiler shows “Try Again! You guessed too high”. That’s mean the random number (i.e., 42) doesn’t fall in the range from 50 to 100. That’s the importance of guessing half of the range. And again, the user guesses half of 50 (Could you tell me why?). So the half of 50 is 25. The user enters 25 as his/her second guess. This time compiler will show, “Try Again! You guessed too small”. That’s mean the integers less than 25 (from 1 to 25) are useless to be guessed. Now the range for user guessing is shorter, i.e., from 25 to 50. Intelligently! The user guessed half of this range, so that, user guessed 37 as his/her third guess.  This time again the compiler shows the output, “Try Again! You guessed too small”. For the user, the guessing range is getting smaller by each guess. Now, the guessing range for user is from 37 to 50, for which the user guessed 43 as his/her fourth guess. This time the compiler will show an output “Try Again! You guessed too high”. So, the new guessing range for users will be from 37 to 43, again for which the user guessed the half of this range, that is, 40 as his/her fifth guess.  This time the compiler shows the output, “Try Again! You guessed too small”. Leaving the guess even smaller such that from 41 to 43. And now the user guessed 41 as his/her sixth guess. Which is wrong and shows output “Try Again! You guessed too small”. And finally, the user guessed the right number which is 42 as his/her seventh guess. After that console must be print a text like this ; `Congratulations! Total Number of Guesses = 7`

#### Algorithm:

1. User inputs the lower limit and upper limit of the range.
2. The compiler generates a random integer between the range and store it in a variable for future references.
3. For repetitive guessing, a `while` loop will be initialized.
4. If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
5. Else if the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
6. Else if the user guessed a number which is not in the range, user must be warned.
7. And if the user guessed the number correct, the user gets a “Congratulations!” output with total number of guesses.

#### Bonus challenge:

So, the minimum number of guesses depends upon range and we can calculate this number. 
Compiler must calculate the minimum number of guessing depends upon the range, on its own. For this, we have a formula:

`Minimum number of guessing = log2(Upper limit – Lower limit + 1)`

Use this formula and print expected minimum number of guess in console.

---
<sub>⭐ Project Author : [GeeksforGeeks](https://www.geeksforgeeks.org/number-guessing-game-in-python/)</sub>
