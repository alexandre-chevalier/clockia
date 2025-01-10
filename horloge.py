import time #import du module time 

def afficher_heure(h, m, s):#fonction afficher heure
     
     print(f"{h:02}:{m:02}:{s:02}", end='\r', flush=True)#format  heure ensur la meme ligne avec les doubles chiffres et ":"

def regler_alarme(h, m, s):#fonction réglage alarme 
    h = int(input("rentrer heures: ")) #heure alarme rentré par utilisateur
    m = int(input("rentrer minutes:"))
    s = int(input("rentrer secondes:"))

    return (h, m, s) # retourne l heure de l alarme sous forme de tuple 
 




def main(): #fonction principale qui execute le program
    s = 0 #variable secondes
    m = 0 #variable minutes
    h = 0 #variable heures
   

    alarme = regler_alarme(h, m, s) #reglage heure alarme a remplir dans les parentheses par moi meme



    while True: #boucle infini = tant que sinon ca s arrete
        s += 1 #ajoute 1 a chaque fois que la boucle tourne
       
        if s == 60: # quand c est egale a 60
            s = 0 #reviens a 0
            m += 1 #ajoutes 1

        if m == 60:
            m = 0 #reviens a 0
            h += 1 # ajoutes 1

       

        afficher_heure(h, m, s)# affiche l heure au format correct

        if (h, m, s) == alarme: #si h actuelle = h alarme message se declenche
           print("Alarme !")
           break # arrete la boucle si l alarme est declenchée
          #alarme = None #reinitialise l alarme pour qu elle s arrete 

        time.sleep (1) #attend 1 scd avant de recommencer la boucle 

main() #appelle la fonction pour lancer le programme

