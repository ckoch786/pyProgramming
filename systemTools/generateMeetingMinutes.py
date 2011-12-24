# An application that takes in txt files as input and generates HTML tables o# or lists 
"""NOTE:  
        os.chdir(path)    <==> cd
	os.listdir(path)  <==> ls
	os.getcwd()       <==> pwd
	os.uname()        <==> ?
        os.open(path ?)   <==> ?
        

"""

import os



class genMeetingMin:
    private __pathTXT
    private __txtFiles
    def __init__(self):
            
     


    def genMeetingList(self):
        __txtFiles = os.listdir(pathTXT)


    def setPathTXT(self, argsv):
       osName = os.uname()

       if osName == 'Linux':
          __pathTXT = "/home/terah/StudentGovernment/TEMPFILES/"
       #elif osName == 'Microsoft':
        #   pathTXT = "\" #TODO
       else:
	   print "Sux to be u!"
        
