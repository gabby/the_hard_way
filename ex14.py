from sys import argv

script, user_name, saying = argv
prompt = '> '

print "Hi %s, i'm the %s script. %s!" % (user_name, script, saying)
print "I'd like to ask you a few questions."

print "Do you like me %s? %s!" % (user_name, saying)
likes = raw_input(prompt)

print "Where do you live %s? %s!" % (user_name, saying)
lives = raw_input(prompt)

print "what kind of computer do you have? %s!" % (saying)
computer = raw_input(prompt)
 
print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. Nice.
%s!
""" % (likes, lives, computer, saying)

likes1 = raw_input("Do you like me %s? %s! " % (user_name, saying))
lives1 = raw_input("Where do you live %s? " % user_name)
computer1 = raw_input("What kind of computer do you have? %s! " % saying)

print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. Nice.
%s!
""" % (likes1, lives1, computer1, saying)

