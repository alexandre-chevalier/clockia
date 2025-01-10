def afficher_heure():
    reglage_heure = input("Appuyez sur 1 si vous voulez régler vous-même l'heure ou 2 pour le réglage auto : ")

    if reglage_heure == '1':  # Si l'utilisateur veut régler l'heure manuellement
        H = int(input("Entrez l'heure actuelle : "))
        M = int(input("Entrez les minutes : "))
        S = int(input("Entrez les secondes : "))
        #print (f"{H:02}:{M:02}:{S:02}")
        print(f"{H:02}:{M:02}:{S:02}", end="\r")  # Affichage formaté de l'heure entrée par l'utilisateur

    elif reglage_heure == '2':  # Si l'utilisateur choisit le réglage automatique
        import datetime
        now = datetime.datetime.now()  # Récupère l'heure actuelle
        H = now.hour  # Heure actuelle
        M = now.minute  # Minute actuelle
        S = now.second  # Seconde actuelle
        print(f"{H:02}:{M:02}:{S:02}", end="\r")  # Affiche l'heure actuelle dans le format HH:MM:SS

# Appel de la fonction
#afficher_heure()
def set_alarm(h_alarme, m_alarm):
    h_alarm=int(input("entrez l'heure pour l'alarme"))
    m_alarm=int(input("entrez les minute pour l'alarme"))
    print("alerte bip bip bip")


#boucle de l'alarme
def main()    