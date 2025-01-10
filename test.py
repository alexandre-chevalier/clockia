from datetime import datetime
import time

def display_hour(timer):
    print(f"il est : {timer[0]:02}:{timer[1]:02}",end="\r")

        

def alarm(hour, alarm):
    if hour[0] == alarm[0] and hour[1] == alarm[1]:
        print(f"il est {hour[0]:02}:{hour[1]:02}")
        

def main():
    
    form_choice     = input("voulez vous changer de format d'heure ? Y/N").upper()
    alarm_hour      = int(input("entrez heure pour l'alarme :  "))
    alarm_minutes   = int(input("entrez minutes pour l'alarme :  "))
    
    
    while True:
        current_hour = time.localtime()
        c_hours  = current_hour.tm_hour
        c_minu   = current_hour.tm_min
        c_seco   = current_hour.tm_sec

        
        if c_hours == 0:
            current_hour_tuple = [12, c_minu]
            alarm_tuple        = [12, alarm_minutes]
        elif c_hours < 12:
            current_hour_tuple = [c_hours,c_minu]
            alarm_tuple        = [alarm_hour,alarm_minutes]
        elif c_hours == 12:
            current_hour_tuple = [12, c_minu]
            alarm_tuple        = [12, alarm_minutes]
        elif c_hours> 12:
            current_hour_tuple = [c_hours - 12, c_minu]
            alarm_tuple        = [alarm_hour - 12, alarm_minutes]

        display_hour(current_hour_tuple)
        alarm(current_hour_tuple,alarm_tuple)

        time.sleep(1)
        

main()