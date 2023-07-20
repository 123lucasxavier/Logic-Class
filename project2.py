'''
Write a program that, upon initiation, generates a random number from 1 to 10 and allows the user to guess a number until the randomly generated number at the start of the program is guessed correctly.

The program should indicate whether the guess was above, below, or equal to the randomly generated number at the beginning of the program.

Critically analyze the problem and find out:
(Try explaining this problem to yourself out loud and ask for more information/investigate further until you fully understand the problem.)
 
 1. What are the required input data?
- Random number from 1 to 10
- User's guess
2. What should I do with this data?
- I should compare the user's guess with the random number generated at the beginning of the program and indicate whether the guess was greater, smaller, or equal to the generated random number.
3. What are the constraints of this problem?
- A random number from 1 to 10.
4. What is the expected output?
- The expected output is that the program should inform whether the guess was above, below, or equal to the randomly generated number at the beginning of the program.
5. What is the sequence of steps to be taken to achieve the expected result?
Input random number from 1 to 10.
Input user's guess.
If the guess is greater than the random number
  print "Guess was higher than the generated value."
If the guess is smaller than the random number
  print "Guess was lower than the generated value."
If the guess is equal to the random number
  print "You got it!"
'''

import random

random_number = random.randint(1,10)
got_it = False

while got_it == False:
  guess = int(input('Guess a number from 1 to 10'))
  if guess > random_number:
    print('Guess was higher than the generated value.')
  elif guess < random_number:
    print('Guess was lower than the generated value.')
  elif guess == random_number:
    got_it = True
    print('You got it!')