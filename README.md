# tictactoe
Simple 2-player tic-tac-toe game in Python
This is a very simple implementation of a tic-tac-toe game. Pushing this to GitHub was mainly an exercise in getting familiar with Git.
That being said, I would like to come back to this when I'm more proficient with Python and implement some more features (such as a single-
player mode against an AI), however I also want to preserve it as it's the most complex coding challenge I've done so far and I'm proud
to see it working, and would love to have it there to compare my later projects against.

The main issue that I know about but don't currently feel like fixing is that when the move() function is called, any input that isn't a
number will cause an error and the program to terminate. I tried to mess around with the function by adding in an .isnumeric() check on
the user input and then adding an if/else statement, but that broke the program. I'm confident that I could figure it out with a little
time dedicated to it, but this program was mainly a way to test myself on loops, control flow, and functions, so I'm pretty keen to move
on. This issue is something I'll address if and when I come back to the program to add an AI.

Another issue is that when a user enters an invalid input, whether it be an interger outside the range of 1-9 or a square already taken,
the program will recognise that and notify the user, however it will also skip their turn. I partly want to leave that in as a way of
penalising incorrect inputs, but that's most likely just me being lazy. Again, that's something that I'll look into at a later date. I have no idea how you found this if you're reading this README, but if you'd like to try your hand at it then you're absolutely welcome to tackle these issues on your own. 
