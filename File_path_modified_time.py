#Code will return the full file path and name along with the modified time stamp

import os
import datetime

filenamelist=[]

#function will disply the file with path

def getfilesnames(path):
    #print path
    for roots,dirs,files in os.walk(path):
        for f1 in files:
            temp=(roots+"\\"+f1)
            filenamelist.append(temp)
           # print filenamelist
            

#function will return the file modified date
            
def getfiledate(filename):
     t= os.path.getmtime(filename)      
     return datetime.datetime.fromtimestamp(t)
        
path="C:\Users"  #in case of windows write proper path like "c:\" in case of unix type "."
getfilesnames(path)
for i in filenamelist:
    #print i
    print i+' --   '+str(getfiledate(i))
    