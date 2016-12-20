# print "How old are you?",
age = raw_input("How old are you? ")
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old %r tall and %r heavy." % (
    age, height, weight)
# %r makes it so when 6'2" is put in it prints '6\'2"' like raw format
