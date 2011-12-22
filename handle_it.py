# Handle it
# Demonstrates handling exceptions
"""
#try/except
try:
    num = float(raw_input("Enter a number: "))
except(ValueError):
    print "That was not a number!"
"""

# Handle multiple exceptions
#print
#for value in (None, "Hi!"):
try:
    value  = raw_input("\nEnter a number: ")
    print "Attempting to convert", value, "-->",
    print float(value)
    #except(TypeError, ValueError):
     #   print "Something went wrong"
     # Or you can use

except(TypeError):
    print "I can only convert a string or a number!"
except(ValueError), e: # Where e is the exceptions argument
    print "I can only convert a string of digits!\n", e
	
else:
    print "You entered the number", value 

raw_input("\n\nPress the enter key to exit.")

