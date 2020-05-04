import serial
from serial import SerialException
import time
import numpy as np
from findcomport import serial_ports

p=serial_ports()
port=str(p[0]) #COM port to which arduino is connected to

try:
   arduino = serial.Serial(port, 57600, timeout=.1) #open the port
except SerialException:
    arduino.close()
    arduino.open()

file=str(input("Enter the filename:"))
arr=[]
time.sleep(2)
t = time.time()+5

while True:
    if time.time() > t:
        break
    
    val=(arduino.readline()[:-2]) #aquire the signal for 5 seconds
    try: 
        arr.append(int(val))
    except ValueError:  
        time.sleep(0.01)
    
for i in arr:
    if i>1000:
        idx=arr.index(i)
        arr.pop(idx)

myarray=np.array(arr)
np.savetxt(file,myarray) #save the signal obtained as a .csv file

arduino.close() #close the connection
