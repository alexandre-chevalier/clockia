import time
import datetime

def afficher_heure(H, M, S, format_heure):
    """Affiche l'heure sous la forme choisie : HH:MM:SS en 12h ou 24h avec strftime."""
    # Créer un objet datetime avec l'heure, les minutes et les secondes
    now = datetime(2025, 1, 1, H, M, S)  # On prend une date arbitraire, l'heure est ce qui nous intéresse
    
    if format_heure == '24':
        # Format 24 heures
        print(f"{H:02}:{M:02}:{S:02}", end="\r")
    elif format_heure == '12':
        # Format 12 heures (AM/PM)
        print(now.strftime("%I:%M:%S %p"), end="\r")

def regler_alarme():
    """Permet de régler l'alarme et retourne l'heure et les minutes de l'alarme."""
    alarme_heure = int(input("Entrez l'heure de l'alarme : "))
    alarme_minute = int(input("Entrez les minutes de l'alarme : "))
    return alarme_heure, alarme_minute

def alerte_alarme():
    """Affiche le message d'alerte lorsque l'alarme sonne."""
    print("\nALERTE ! bip bip bip !!!")

def main():
    """Affiche l'heure en temps réel et alerte quand l'alarme sonne."""
    # Choisir le format de l'heure uniquement si on choisit le réglage auto
    reglage_heure = input("Appuyez sur 1 si vous voulez régler vous-même l'heure ou 2 pour le réglage auto : ")

    if reglage_heure == '1':  # Réglage manuel de l'heure (format 24h)
        H = int(input("Entrez l'heure actuelle (format 24h) : "))
        M = int(input("Entrez les minutes : "))
        S = int(input("Entrez les secondes : "))
        format_heure = '24'  # Forcer le format 24h
    elif reglage_heure == '2':  # Réglage automatique de l'heure
        now = datetime.now()
        H = now.hour
        M = now.minute
        S = now.second
        # Choisir le format de l'heure
        format_heure = input("Choisissez le format de l'heure (24 pour 24h, 12 pour 12h): ")

    # Réglage de l'alarme
    alarme_heure, alarme_minute = regler_alarme()

    alarme_sonnee = False  # Pour savoir si l'alarme a déjà sonné

    while True:
        # Incrémentation des secondes
        S += 1

        # Gérer le passage d'une minute à l'autre
        if S == 60:
            M += 1
            S = 0

        # Gérer le passage d'une heure à l'autre
        if M == 60:
            H += 1
            M = 0

        # Réinitialisation de l'heure si elle dépasse 23 heures
        if H == 24:
            H = 0

        # Affichage de l'heure avec le format choisi
        afficher_heure(H, M, S, format_heure)

        # Vérification si l'heure actuelle correspond à l'heure de l'alarme
        if H == alarme_heure and M == alarme_minute and not alarme_sonnee:
            alerte_alarme()  # Affichage de l'alerte
            alarme_sonnee = True  # On marque que l'alarme a sonné, mais on ne l'arrête pas

        time.sleep(1)  # Attente d'une seconde avant de mettre à jour l'heure

# Appel de la fonction main pour lancer le programme
main()
