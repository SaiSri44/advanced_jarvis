import os
from playsound import playsound
import datetime

extracted_time = open("C:\\Users\\angaj\\OneDrive\\Desktop\\jarvis2\\features of jarvis\\data.txt",'rt') 
time = extracted_time.read()
Time = str(time)

delete_time = open("C:\\Users\\angaj\\OneDrive\\Desktop\\jarvis2\\features of jarvis\\data.txt",'r+')
delete_time.truncate(0)
delete_time.close()

def alarm_ring(Time) :
    alarm_time = Time 
    while True :
        current_time = datetime.datetime.now().strftime("%H:%M")  
        if current_time == alarm_time :
            print("Time to wake up sir") 
            playsound("C:\\Users\\angaj\\OneDrive\\Desktop\\jarvis2\\database\\sounds\\jarvis wake up alarm.mp3") 
        if current_time > alarm_time :
            print("The alaram closed") 
            break 
            
alarm_ring(Time)      



