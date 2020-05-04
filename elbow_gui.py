import numpy as np
import serial
from serial import SerialException
import time
from findcomport import serial_ports
from readcsv import getcsv
from preprocessing import preprocessing
from features import getfeatures
from sklearn.neighbors import KNeighborsClassifier

p=serial_ports()
port=str(p[0]) #COM port to which arduino is connected to

try:
   arduino = serial.Serial(port, 57600, timeout=.1) #open the port
except SerialException:
    arduino.close()
    arduino.open()

data=np.loadtxt(open("elbow_feature_set.csv", "rb"), delimiter=",")
file='Samples/Girls/sample.csv'

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

X = data[:,[0,3,4,5,6]]  #top 5 features obtained
y = data[:,16] #labels
emg = getcsv(file)
emg_rectified=preprocessing(emg) #pre-process the signal
feat_array=np.matrix(getfeatures(emg_rectified)) #obtain the feature set 

# training the model on training set
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
 
# making predictions on the testing set
y_pred = knn.predict(feat_array[0,[0,3,4,5,6]])
print(y_pred)
t= '1'.encode('ascii','ignore')

if (y_pred==4):
	t = '4'.encode('ascii','ignore')
elif (y_pred==5):
	t = '5'.encode('ascii','ignore')
elif (y_pred==6):
	t = '6'.encode('ascii','ignore')
elif (y_pred==7):
	t = '7'.encode('ascii','ignore')
elif (y_pred==8):
	t = '8'.encode('ascii','ignore')


dat = ""
while not arduino.is_open:
	pass
arduino.write(t) #send predicted output to the arduino

arduino.close() #close the connection
