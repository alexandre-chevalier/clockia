def afficher_heure():
    reglage_heure = input("Appuyez sur 1 si vous voulez régler vous-même l'heure ou 2 pour le réglage auto : ")

    if reglage_heure == '1':  # Comparer avec des chaînes de caractères
        H = int(input("Entrez l'heure actuelle : "))
        M = int(input("Entrez les minutes : "))
        S = int(input("Entrez les secondes : "))
    print(f"{H:02}:{M:02}:{S:02}", end="\r")  # Affichage formaté

afficher_heure()    