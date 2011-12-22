# Pickle it
# Demonstrates pickling and shelving data
import cPickle, shelve


print "Pickling lists"
variety = ["sweet", "hot", "dill"]
shape   = ["whole", "spear", "chip"]
brand   = ["Claussen", "Heinz", "Vlassic"]

pf = open("pickles1.dat", "w")
cPickle.dump(variety, pf)
cPickle.dump(shape, pf)
cPickle.dump(brand, pf)
pf.close()

print "\nUnpickling lists."
pf = open("pickles1.dat", "r")
variety = cPickle.load(pf)
shape   = cPickle.load(pf)
brand   = cPickle.load(pf)

print variety, "\n", shape, "\n", brand
pf.close()


print "\nShelving lists"
pickles = shelve.open("pickels2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"]   = ["whole", "spear", "chip"]
pickles["brand"]   = ["Claussen", "Heinz", "Vlassic"]

pickles.sync() # make sure data is written

print "\nRetrieving the lists from a shelved file:"
for key in pickles.keys():
    print key, "-", pickles[key]

pickles.close()

raw_input("\n\nPress the enter key to exit.")
