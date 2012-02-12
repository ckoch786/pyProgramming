#
 # generateMeetingMinutes.py
 #* Copyright (C) 2011-2012 Cory Koch.
 #*
 #* This file is part of StudentGovernmentTools.
 #* 
 #* StudentGovernmentTools is free software: you can redistribute it and/or modify it
 #* under the terms of the GNU General Public License as published by the
 #* Free Software Foundation, either version 3 of the License, or
 #* (at your option) any later version.
 #* 
 #* StudentGovernmentTools is distributed in the hope that it will be useful, but
 #* WITHOUT ANY WARRANTY; without even the implied warranty of
 #* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 #* See the GNU General Public License for more details.
 #* 
 #* You should have received a copy of the GNU General Public License along
 #* with this program.  If not, see <http://www.gnu.org/licenses/>.
 #*/
# An application that takes in txt files as input and generates HTML tables o# or lists 


"""NOTE:  
        os.chdir(path)    <==> cd
	os.listdir(path)  <==> ls
	os.getcwd()       <==> pwd
	os.uname()        <==> ?
        os.open(path ?)   <==> ?
        os.

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
        
