# replace one %d with an int and set variable x to result
x = "There are %d types of people." % 10
# set variable binary with a string
binary = "binary"
# set variable do_not with a string
do_not = "don't"
# replace two %s with strings and set variable y to result
y = "Those who know %s and those who %s." % (binary, do_not)

# print the string x is set to
print x
# print the string y is set to
print y

# replace %r with x string
print "I said: %r" % x
# replace %s with y string
print "I also said: '%s'" % y

# set variable hilarious to boolean value False
hilarious = False
# set variable joke_evaluation to
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the string joke_evaluation replacing %r with hilarious
print joke_evaluation % hilarious

# set variable w to a string
w = "This is the left side of..."
# set variable e to a string
e = "a string with a right side."

# print w with e appended to the end
print w + e
