# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    numbers.txt = open('numbers.txt', 'r')

    contents = infile.read()

    print(contents)

    infile.close()

    sum_numbers += sum(contents)
    print(sum_numbers)
    print('In the sum_numbers_from_file function')
except IOError:
    print('An error occured trying to read the file', filename)
except ValueError:
    print('An error occured trying to produce the value from the file', filename)

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
