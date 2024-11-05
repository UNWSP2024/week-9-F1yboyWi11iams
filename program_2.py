# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

def rand_numbers():
  for count in range(input(int('Please specify how many numbers this file will hold (up to, but not exceeding, 1000): '))):
    if count > 1000 or count < 0, print('ERROR: Must enter a number less than 1000 but greater than 0')
    else:
      number = random.randint (1, 500)
      print(f'The number is {number}.')

rand_numbers():
