x = "There are %d types of people." % 10 
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
# 1: string inside a string
print y

# 2: string inside a string
print "I said: %r." % x
# 3: string inside a string
print "I also said: %s." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 

#4: string inside a string, forcing it with %r
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#5: string inside a string 
print w + e