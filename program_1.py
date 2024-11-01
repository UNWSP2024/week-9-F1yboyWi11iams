# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    infile = open('names.txt', 'r')

    file_contents = infile.read()
    infile.close()
    print(file_contents)
    count = 0
    my_string = file_contents
    for ch in my_string:
        count += 1
    count_file_lines = my_string
    print(f'In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
