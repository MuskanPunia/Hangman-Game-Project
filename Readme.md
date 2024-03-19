PROJECT TITLE - Hangman Project 
Game Description : This project is a Hangman Project Game.It is a guessing game for two or more players.Here, we have designed it for single user. The player thinks of a word and tries to guess it by suggesting letters. If the user is able to guess the word correctly , the user wins. The objective of the game is to expand vocabulary through playing with words, making it a fun way of learning. TEAM MEMBERS : Manager : Muskan (2310990743) Developer : Harshita Lamba (2310990687) Tester: Kashish (2310990710)

Instructions for running the game: Our code generates a random word based on a theme, which has to be guessed by the player. The screen will display blanks (short lines) for each letter of the word. Then the player is asked to guess a letter, if the letter appears in the word, the blanks get replaced by the letter at everyplace it appears in the word. If the guessed letter does'nt exist in the word,we cross out the lifelines, which are basically the number of chances.The player will continue guessing the letters until he/she guesses the whole word or loses the game.To make it interesting, we have added a hangman figure. As the player guesses a wrong letter, one element gets added to the hangman. If the user loses, the screen displays the whole diagram of a hangman.

VERSION-1: The approach is good, but there are few errors I'd like to highlight:

1. Once the player guesses the whole word correctly, the program is supposed to declare the user as winner. However, the code is still running until the number of chances reduces to zero. Then, it asks the user if they want to play again without telling them if they won or lose.
2.The figures of hangman are there in the code, but they are not being displayed on the screen as and when required, which needs to be done in the right way. As the name suggests, the game revolves around hangman, so the errors must be rectified to make the figures visible.
3. The words are quite simple. I'd recommend to add some good vocabulary words to make the game more interesting and challenging
4. If the user does'nt guess anything,it says congratulations , which denotes a correct guess. This is a big mistake that needs to be taken care of.
5. The random words are generated inside the loop, which means every time the loop runs, it generates a new word.Put that outside the loop.
6. If the player loses the game, it continues to ask the user to guess a letter. It should terminate the game right away.
The blanks were not there, make them visible using loops by counting the number of letters in the word and replace them by the letter as the player makes a right guess

VERSION-2:
1. The figures are visible now.
2. We've added hints in case the user can't make a right guess for a couple of times. They might feel demotivated. so to cheer them up, we provide them hints which basically tells the features of the word, for instance if it is a country, it'd tell them about the capital of the nation, etc, a good approach to expand knowledge about the subject.
3. The simple words have been replaced with pretty good ones. Now, they are based on a specific theme like the name of countries.
4. The error related to breaking the loop when the user wins, have been taken care of.
5. The GUI is better now as the input of letter is taken in the next line, increasing the readability and convienience.
6. The game won't congratulate the user again and again for making a right guess. It'd congratulate them at the end when they win.

VERSION-3:
1. All the errors have been rectified and the game runs smoothly without any technical interruptions.
2. We've added emojis to make it look more fun and interactive.
3. Corrected the errors regarding blanks.
4. Worked more on the user interface to make it look more better.
5. made the hints more precise and easy to comprehend by the player to cheer them up to keep playing.

