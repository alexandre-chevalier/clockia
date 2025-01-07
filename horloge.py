import time #import du module time 

def afficher_heure(h, m, s):#fonction afficher heure
     print(f"{h:02}:{m:02}:{s:02}", end='\r', flush=True)#format  heure ensur la meme ligne avec les doubles chiffres et ":"

def regler_alarme(h, m, s):#fonction réglage alarme 
    return (h, m, s) # retourne l heure de l alarme sous forme de tuple 
 
    



def main(): #fonction principale
    s = 0 #variable secondes
    m = 0 #variable minutes
    h = 0 #variable heures
   # alarme = None # variable alarme, commence a none

    alarme = regler_alarme(0, 0, 3) #reglage heure alarme a remplir dans les parentheses

    while True: #boucle infini
        s += 1 #ajoute 1 a chaque fois que la boucle tourne
       
        if s == 60: # quand c est egale a 60
            s = 0 #reviens a 0
            m += 1 #ajoutes 1

        if m == 60:
            m = 0 #reviens a 0
            h += 1 # ajoutes 1

        #print (f"{h:02}:{m:02}:{s:02}", end='\r', flush=True)

        afficher_heure(h, m, s)# affiche l heure au format correct

        if (h, m, s) == alarme: #si h actuelle = h alarme message se declenche
           print("Alarme !")
           break # arrete la boucle si l alarme est declenchée
          #alarme = None #reinitialise l alarme pour qu elle s arrete 

        time.sleep (1) #attend 1 scd avant de recommencer la boucle 

main() #appelle la fonction pour lancer le programme

