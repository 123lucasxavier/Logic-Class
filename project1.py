'''
Create a program that takes a number as input and prints its factorial.

To develop an algorithm:
Critically analyze the problem and find out:
(Try explaining this problem to yourself out loud and ask for more information/investigate further until you fully understand the problem.)

1 - What are the required input data?
Number
2 - What should I do with this data?
Calculate the factorial of the entered number and print it
3 - What are the constraints of this problem?
The number must be an integer and also be positive.
4 - What is the expected output?
The factorial of the entered number is expected to be displayed
5 - What is the sequence of steps to be taken to achieve the expected result?

input number
if number > 0
if number = integer 
factorial = 1
loop from 1 to the number
  factorial = factorial * number
print(factorial)
'''

number = int(input('Type a number'))
if number > 0:
  factorial = 1
  for item in range (1,number +1):
    factorial = factorial * item
  print(factorial)