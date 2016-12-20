def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def arithmetic(num1, num2):
    print "%d + %d = %d" % (num1, num2, num1 + num2)
    print "%d - %d = %d" % (num1, num2, num1 - num2)
    print "%d * %d = %d" % (num1, num2, num1 * num2)
    print "%d / %d = %d" % (num1, num2, num1 / num2)

print "Numbers directly:"
arithmetic(3,6)

print "Variables:"
num1 = 4
num2 = 5
arithmetic(num1,num2)

print "Math inside"
arithmetic(3+3, 6+9)

print "Math and Variables"
arithmetic(5+num1, 6+num2)
