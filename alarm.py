from datetime import datetime
import time
import random

hours = ["10","20","10"]

def alarm_message(time):
    print(time)

    ##valeur que l'utilisateur rentre pour setup l'alarme
    hour = int(input("enter the hour you want for the alarm "))
    minutes = int(input("enter the minutes you want for the alarm "))
    seconds = int(input("enter the seconds you want for the alarm "))


    if hour > 59 and minutes > 59 and minutes > 59: 
        alarm_target(time)
    else:        
        link_alarm=[hour,minutes, seconds]


    times   = f"{time[0]}:{time[1]}:{time[2]}"
    alarms  = f"{hour}:{minutes}:{seconds}"
    
 
    if times == alarms:
        print(f"il est {hour}:{minutes}:{seconds}  bip biiip biiiiip BIIIIIIIIIIIP votre alarme sonne")
    else:
        print("ce n'est pas encore l'heure")



alarm_message(hours)