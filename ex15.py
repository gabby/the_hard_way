#using python import commands
from sys import argv
#argv in this case will be a filename
script, filename = argv
#assigning the variable txt to open the filename 
txt = open(filename)
#we print a string and include the name of the filename we passed
print "Here's your file %r:" % filename
#using python command 'read()' but assigning this command to a file using a '.'
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()


#first set of code simply takes the filename passed thru in the agrv and opens 
#second set of code gets the filename from a raw_input command prompting using to 
#input and provide a filename 
