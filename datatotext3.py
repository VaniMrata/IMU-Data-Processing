import serial
import time
import datetime
import sys
from queue import Queue
ser=serial.Serial(port='COM5', baudrate=115200, timeout=0)
time.sleep(1)
q=Queue(maxsize=0)
global newdata
i=0        
f1=open(f"Extracted data (x) {i}.csv", "a")
f1.write("TIME                        ROLL    PITCH  HEAVE")
f1.write('\n')
f1.close()
def header():
    f1=open(f"Extracted data (x) {i}.csv", "a")
    f1.write("TIME                        ROLL    PITCH  HEAVE")
    f1.write('\n')
    f1.close()
    
while True:
    while (ser.inWaiting()==0):
            pass
    datapacket=ser.readline()
    datapacket=str(datapacket, 'utf-8')
    q.put(datapacket)
    time.sleep(0.1)
    data=q.get()
    dataarray=data.split(',')
    try:
        newdata=[datetime.datetime.now(), dataarray[4], dataarray[5], dataarray[6]]
        newdata=','.join([str(elem) for elem in newdata])
        f3=open("analytics (x).txt", "a")
        res=sys.getsizeof(newdata)
        f3.write(str(res))
        f3.write('\n')
        f1=open(f"Extracted data (x) {i}.csv", "a")
        f2=open(f"Extracted data (x) {i}.csv", "r")
        f1.write(newdata)
        f1.write('\n')
        if len(f2.readlines())==3000:
            i+=1
            f3.write(f"file{i} starts \n")
            header()
            f1.close()
            f2.close()
            q.task_done()
            ser.flushInput()
    except IndexError as e:
        f3.write(str(e))
        f3.close()
        

