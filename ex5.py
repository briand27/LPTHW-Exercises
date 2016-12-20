name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky
print "If I add %d, %d, and %d I get %d" % (
    age, height, weight, age + height + weight)

height_centimeters = height * 2.54
weight_kilogram = weight * .454

print "Height in centimeters is %f" % height_centimeters
print "Weight in kilograms is %f" % weight_kilogram
