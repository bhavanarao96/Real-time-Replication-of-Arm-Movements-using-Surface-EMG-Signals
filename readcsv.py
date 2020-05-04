import csv
import numpy as np

def getcsv(filename): #load csv file into a numpy array
    with open(filename,newline='') as csvfile:
     reader = csv.reader(csvfile)
     values=[]
     for row in reader:
         for i in row:
             values.append(float(i))  
    myarray=np.asarray(values)
    myarray=np.array(myarray)
    return(myarray) #returns the numpy array

     
