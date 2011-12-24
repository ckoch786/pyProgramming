# Read it
# Demonstrates reading from a text file

fileNM="read_it.txt"

print "Opening and closing the file"
tf = open(fileNM, "r")
tf.close()

print "\nReading characters from the file"
tf = open(fileNM, "r")
print tf.read(1)
print tf.read(5)
tf.close()

# Note: read() with no args returns the whole doc as a string
print "\nReading the entire file at once"
tf = open(fileNM, "r")
whole_thing = tf.read()
print whole_thing
tf.close()

print "\nReading characters from a line"
tf = open(fileNM, "r")
print tf.readline(1)
print tf.readline(5)
tf.close()

print "\nReading one line at a time"
tf = open(fileNM, "r")
print tf.readline()
print tf.readline()
print tf.readline()
tf.close()

# Note: readlines() returns a list of strings where the strings are the 
#lines in the doc
print "\nReading the entire file into a list"
tf = open(fileNM, "r")
lines = tf.readlines()
print lines
print len(lines)
for line in lines:
    print line

tf.close()

print "\nLooping through the file, line by line"
tf = open(fileNM, "r")
for line in tf:
    print line

tf.close()

raw_input("\n\nPress the enter key to exit")



