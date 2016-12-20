# imports System
from sys import argv

# creates variables script and input_file for arguments
script, input_file = argv

# define a function that takes in a file to read
def print_all(f):
    print f.read()

# define a function that takes in a file to seek
def rewind(f):
    f.seek(0)

# defines a function that prints out the given line of a given file
def print_a_line(line_count, f):
    print line_count, f.readline()

# creates a variable that represents the open input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# calls print_all on the given file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# calls rewind on the given current_file
rewind(current_file)

print "Let's print three lines:"

# sets current_line to 1 the prints that line of the current_file
current_line = 1
print_a_line(current_line, current_file)

# sets the current_line one higher then prints that line of the current_file
current_line += 1
print_a_line(current_line, current_file)

# sets the current_line one higher again then prints that line of
# the current_file
current_line += 1
print_a_line(current_line, current_file)
