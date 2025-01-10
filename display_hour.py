import time
  

def display_hour():
    #regler l'heure de depart
    H=int(input("entrez l'heure actuel"))
    M=int(input("entrer les minutes"))
    S=int(input("entrer les secondes" ))
    # Demander à l'utilisateur de définir l'heure de l'alarme
    alarme_H = int(input("Entrez l'heure de l'alarme (0-23) : "))
    alarme_M = int(input("Entrez les minutes de l'alarme (0-59) : "))
    alarme_S = int(input("Entrez les secondes de l'alarme (0-59) : "))
    heure_alarm = (alarme_H,alarme_M,alarme_S)
    heure=(H, M, S,)
    #boucle de comptage du temps
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
        #affichage du temps
        print(f"{H:02}:{M:02}:{S:02}", end="\r") #affiche le temps au format HH:MM:SS et ecrase l'ancienne valeur et affiche la nouvelle sur la meme ligne
         # Vérifier si l'heure actuelle correspond à l'alarme
        if H == alarme_H and M == alarme_M and S == alarme_S:
                print("ALERTE :bip bip bip!", end="\r") 
        
        time.sleep(1)  


display_hour()