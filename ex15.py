# import something to read in the arguments of the file
from sys import argv

# save the arguments in script and filename
script, filename = argv

# open the given file (second argument) and save it in a variable
txt = open(filename)

# prints the file's name
print "Here's your file %r:" % filename
# prints the contents of the file
print txt.read()

print "Type the filename again:"
# ask for the file again and take in the input
file_again = raw_input("> ")

# save the given file to a new variable txt_again
txt_again = open(file_again)

# print contents of the second given file
print txt_again.read()

txt.close()
txt_again.close()
