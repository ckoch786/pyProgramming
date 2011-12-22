# Write it
# Demonstrates writing to a text file

print "Creating a text file with the write() method"
tf = open("write_it.txt", "w")
tf.write("Line 1\n")
tf.write("This is line 2\n")
tf.write("That makes this line 3\n")
tf.close()

print "\nReading the newly created file"
tf = open("write_it.txt", "r")
print tf.read()
tf.close()


# Note: the writelines() method works with a  list of strings
print "\nCreating a text file with the writelines() method"
tf = open("write_it.txt", "w")
lines = ["Line 1\n",
	"This is line 2\n",
	"That makes this line 3\n"]
tf.writelines(lines)
tf.close()

print "\nReading the newly created file"
tf = open("write_it.txt", "r")
print tf.read()
tf.close()

raw_input("\n\nPress the enter key to exit.")
