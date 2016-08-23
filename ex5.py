name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74#centimeters
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = "Brown"
height_cm = height * 2.54
weight_kg = weight * 0.453592

print "Let's talk about %s." % name
print "He's %f centimeters tall." % round(height_cm, 2)
print "He's %f kilos heavy." % round(weight_kg, 2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %f, and %f I get %f." % (age, round(height_cm,2), round(weight_kg, 2), age + round(height_cm, 2) + round(weight_kg, 2))