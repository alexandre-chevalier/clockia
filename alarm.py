from datetime import datetime
import time
import random


def display_hour():
    H=int(input("entrez l'heure :  "))
    M=int(input("entrer les minutes : "))
    S=int(input("entrer les secondes : " ))
    heure=(H, M, S)
    while True:
        S += 1 # on incrémente les secondes
        
        if S==59: # à chaque fois que l'on atteint 60 seconds on incrémente les minutes et on réinitialise la variable seconde
            M += 1
            S = 0
            if M == 59: #pareil pour les minutes
                H += 1
                M = 0
                if H==23: #on réinitialise l'heure au bout de 24H
                    H = 0

        print(f"{H:02}:{M:02}:{S:02}", end="\r") #affiche le temps au format HH:MM:SS et ecrase l'ancienne valeur et affiche la nouvelle sur la meme ligne
        time.sleep(1)  

def main():
    ##valeur que l'utilisateur rentre pour setup l'alarme
    hour = int(input("enter the hour you want for the alarm "))
    minutes = int(input("enter the minutes you want for the alarm "))
    seconds = int(input("enter the seconds you want for the alarm "))

    link_alarm=[hour,minutes, seconds]

    alarms  = f"{hour}:{minutes}:{seconds}"
    print("so sally, can wait")
    """
    if times == alarms:
        print(f"il est {hour}:{minutes}:{seconds}  bip biiip biiiiip BIIIIIIIIIIIP votre alarme sonne")
    else:
        print("ce n'est pas encore l'heure")
        """
    display_hour()

    

main()