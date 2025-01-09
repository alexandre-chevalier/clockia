import time
import winsound

def afficher_heure(choice):
        if choice =="Y":
            heure = time.strftime("%I:%M:%S")
            print(heure)
            time.sleep(1)
        elif choice == "N":
            heure = time.strftime("%H:%M:%S  %p")
            print(heure)
            time.sleep(1)

def main():
   
    form_choice = input("voulez vous l'heure au format AM ? Y/N : ").upper()
    
    ## variable to setup the alarm ##
    hour    = input("entrez heure pour l'alarme :  ")
    minutes = input("entrez minutes pour l'alarme :  ")
    seconds = input("entrez heure pour l'alarme :  ")
    while True:
        afficher_heure(form_choice)
        music = "TheOverview.wav"

        heure = time.strftime("%H:%M:%S %p")
        alarm = time.strftime(f"{hour}:{minutes}:{seconds} %p")
        print(heure +"    "+ alarm)
        
        if heure == alarm :
            print(f"Il est {heure}  reveille toi ")
            winsound.PlaySound(music, winsound.SND_FILENAME)
            

main()