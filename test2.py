from datetime import datetime
import time
import winsound


## the function display the hour with the correct format with the choice of the user ##
def display_hour(choice):
        if choice =="Y":
            hour = time.strftime("%I:%M:%S %p")
            print(hour)
            time.sleep(1)
        elif choice == "N":
            hour = time.strftime("%H:%M:%S")
            print(hour)
            time.sleep(1)

def main():
   
    form_choice = input("voulez vous l'heure au format AM ? Y/N : ").upper()
    display_hour(form_choice)
    music = "TheOverview.wav"

    ## variable to setup the alarm ##
    alarm_hour  = input("entrez heure pour l'alarme :  ")
    minutes     = input("entrez minutes pour l'alarme :  ")
    seconds     = input("entrez heure pour l'alarme :  ")
   
    while True:
        ## the user choose the format of the hour he want ##
        if form_choice == "Y":
            hour = time.strftime("%I:%M:%S %p")
            alarm_am = datetime.strptime(f"{alarm_hour}:{minutes}:{seconds}", "%H:%M:%S")
            alarm = alarm_am.strftime("%I:%M:%S %p")
            print(hour + "    hello   " +alarm )
            time.sleep(1)
        elif form_choice == "N":
            hour = time.strftime("%H:%M:%S")
            alarm = time.strftime(f"{alarm_hour}:{minutes}:{seconds}")
            print(hour +"    "+ alarm)
            time.sleep(1)

        ## conditions to print the message of the alarm ##
        if hour == alarm:
            print(f"Il est {hour}  reveille toi ")
            ## winsound.PlaySound(music, winsound.SND_FILENAME)
            break
            

main()