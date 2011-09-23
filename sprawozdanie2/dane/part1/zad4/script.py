from ctypes import *
import re
import os
  
path = r"d:\studia\informatyka\semestr8\UMiSN\laby\repo\sprawozdanie2\dane\part1\zad4"
fout = open("errors.dat", 'w')
fout.write("#epochs");

data = {}

ls = os.walk(path)
for dirpath, dirnames, filenames in ls:
    filenames.sort()
    for filename in filenames:
        if re.search("[0-9]\.txt", filename):
            fout.write("\t%s" % (filename,))
            fin = open(filename)            
            count = 0
            for line in fin:
                if count > 0:
                    words = line.split()
                    epoch = int(words[0])
                    error = words[1]
                    epochDict = data.setdefault(epoch, {})
                    epochDict.setdefault(filename, error)
                count += 1
             
for epoch in sorted(data.keys()):
    fout.write("\n%d" % epoch ) 
    filenames = sorted(data[epoch])
    for filename in filenames:
        fout.write("\t%s" % (data[epoch])[filename])
    
                

                
                
