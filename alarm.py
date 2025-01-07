from datetime import datetime
import time
import random

hours = [random.randint(9,10),random.randint(9,10),random.randint(9,10)]

def setAlarm():
    
    hour = int(input("enter the hour you want for the alarm "))
    if hour > 23:
        setAlarm()
    else:
        minutes = int(input("enter the minutes you want for the alarm "))
        seconds = int(input("enter the seconds you want for the alarm "))
        if minutes >59 and minutes>59:
            setAlarm()
        else:
            link_alarm=[hour,minutes, seconds]
            print(link_alarm)
            return link_alarm

"""
variable de la fonction alarme:
times
alarms
format_alarms
curren_times
alarm_target

"""

def alarm_message(time, time_alarm):
    print(time)
    print(time_alarm)
    
    times   = f"{time[0]}:{time[1]}:{time[2]}"
    alarms  = f"{time_alarm[0]}:{time_alarm[1]}:{time_alarm[2]}"
    format_alarms = "%H:%M:%S"
    
    current_times   = datetime.strptime(times,format_alarms) 
    alarm_target    = datetime.strptime(alarms, format_alarms)
    print(alarm_target, current_times)
 
    if current_times == alarm_target:
        print(f"il est {time_alarm[0]}:{time_alarm[1]}:{time_alarm[2]}  bip biiip biiiiip BIIIIIIIIIIIP votre alarme sonne")
    else:
        print("ce n'est pas encore l'heure")

alarm_message(display_hour(), setAlarm())