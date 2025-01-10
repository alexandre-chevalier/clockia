# affichage de l'horloge
import time
def horloge():
    # on initialise les variables seconds, minutes, et heures au temps local
    now = time.localtime()
    H = now.tm_hour  # Heure actuelle
    M = now.tm_min   # Minute actuelle
    S = now.tm_sec   # Seconde actuelle
    while True:
        S += 1 # on incrémente les secondes
        
        if S==60: # à chaque fois que l'on atteint 60 seconds on incrémente les minutes et on réinitialise la variable seconde
            M += 1
            S = 0
            if M == 60: #pareil pour les minutes
                H += 1
                M = 0
                if H==24: #on réinitialise l'heure au bout de 24H
                    H = 0
        print(f"{H:02}:{M:02}:{S:02}", end="\r") #affiche le temps au format HH:MM:SS et ecrase l'ancienne valeur et affiche la nouvelle sur la meme ligne
        time.sleep(1)  
horloge()            