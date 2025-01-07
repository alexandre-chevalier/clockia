import time
def display_hour():
    H=int(input("entrez l'heure actuel"))
    M=int(input("entrer les minutes"))
    S=int(input("entrer les secondes" ))
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



display_hour()