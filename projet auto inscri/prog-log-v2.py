# ============================================================
# IMPORTATION DES BIBLIOTHÈQUES
# ============================================================

# Permet de contrôler le clavier et la souris.
import pyautogui

# Permet de faire des pauses.
import time

# Permet de copier/coller l'URL.
import pyperclip

# Permet de choisir des délais aléatoires.
import random


# ============================================================
# CONFIGURATION
# ============================================================

PRENOM = "Lucas"
NOM = "Martin"

JOUR = "5"
ANNEE = "2000"

IDENTIFIANT = "lucas.martin.test12342441"
MOT_DE_PASSE = "Test123456@"


# ============================================================
# FONCTIONS
# ============================================================

def pause():
    # Attend exactement 1 seconde.
    time.sleep(1)


def pause_action():
    # Choisit un délai aléatoire entre 1,5 et 17 secondes.
    delai = random.uniform(1.5, 17)

    # Affiche le délai dans le terminal pour savoir
    # combien de temps le programme attend.
    print(f"Pause : {delai:.2f} secondes")

    # Attend le délai choisi.
    time.sleep(delai)


def taper(texte):
    # Écrit le texte caractère par caractère.
    pyautogui.write(texte, interval=0.1)


def tab():
    # Appuie sur TAB.
    pyautogui.press("tab")

    # Attend un délai aléatoire.
    pause_action()


def entrer():
    # Appuie sur ENTRÉE.
    pyautogui.press("enter")

    # Attend un délai aléatoire.
    pause_action()


def bas():
    # Appuie sur la flèche du bas.
    pyautogui.press("down")

    # Attend 1 seconde.
    pause()


def espace():
    # Appuie sur ESPACE.
    pyautogui.press("space")

    # Attend 1 seconde.
    pause()


def plusieurs_tabs(nombre):
    # Répète TAB plusieurs fois.
    for i in range(nombre):
        tab()


# ============================================================
# DÉBUT DU PROGRAMME
# ============================================================

print("===================================")
print("          DÉBUT DU TEST")
print("===================================")

print()
print("Le programme va commencer dans 3 secondes...")

# Attend 3 secondes.
time.sleep(3)


# ============================================================
# OUVERTURE DE MICROSOFT EDGE
# ============================================================

print()
print("Ouverture de Microsoft Edge...")

# Ouvre la fenêtre "Exécuter" de Windows.
pyautogui.hotkey("win", "r")

# Attend 1 seconde.
pause()

# Écrit "msedge".
pyautogui.write("msedge", interval=0.1)

# Lance Edge.
pyautogui.press("enter")

print("Edge lancé.")

# Attend qu'Edge s'ouvre.
time.sleep(3)


# ============================================================
# METTRE EDGE EN GRAND ÉCRAN
# ============================================================

# Windows + flèche vers le haut maximise Edge.
pyautogui.hotkey("win", "up")

# Attend 1 seconde.
pause()

print("Edge est maintenant maximisé.")


# ============================================================
# LIRE L'URL
# ============================================================

print()
print("Lecture de l'URL...")

try:
    # Ouvre url.txt.
    with open("url.txt", "r", encoding="utf-8") as fichier:
        URL = fichier.read().strip()

except FileNotFoundError:
    print()
    print("ERREUR : url.txt est introuvable.")
    print("Place url.txt dans le même dossier que prog-log-v2.py.")
    input("Appuie sur Entrée pour fermer...")
    raise SystemExit


# Vérifie que l'URL existe bien.
if URL == "":
    print()
    print("ERREUR : url.txt est vide.")
    input("Appuie sur Entrée pour fermer...")
    raise SystemExit


print("URL trouvée :", URL)


# ============================================================
# METTRE L'URL DANS EDGE
# ============================================================

print()
print("Ouverture de l'URL...")

# Sélectionne la barre d'adresse.
pyautogui.hotkey("ctrl", "l")
pause()

# Sélectionne tout.
pyautogui.hotkey("ctrl", "a")
pause()

# Copie l'URL.
pyperclip.copy(URL)

# Colle l'URL.
pyautogui.hotkey("ctrl", "v")
pause()

# Valide.
pyautogui.press("enter")

print("URL envoyée à Edge.")

# Attend 3 secondes.
time.sleep(3)


# ============================================================
# PREMIÈRE ÉTAPE
# ============================================================

print()
print("Première étape...")

# TAB
tab()

# TAB
tab()

# ENTER
entrer()


# ============================================================
# CRÉER UN COMPTE
# ============================================================

print()
print("Navigation vers 'Créer un compte'...")

# 4 TAB.
plusieurs_tabs(4)

# ENTER.
entrer()


# ============================================================
# ENTER SUPPLÉMENTAIRE
# ============================================================

print("Validation supplémentaire...")

# ENTER.
entrer()


# ============================================================
# PRÉNOM / NOM
# ============================================================

print()
print("Écriture du prénom...")

# Le curseur est déjà dans la case prénom.
taper(PRENOM)

print("Écriture du nom...")

# Passe au nom.
tab()

# Écrit le nom.
taper(NOM)


# ============================================================
# PAGE SUIVANTE
# ============================================================

print("Validation prénom / nom...")

entrer()


# ============================================================
# DATE
# ============================================================

print()
print("Nouvelle page : date...")


# ============================================================
# JOUR
# ============================================================

print("Écriture du jour...")

# TAB
tab()

# Écrit le jour.
taper(JOUR)


# ============================================================
# MENU
# ============================================================

print("Navigation dans le menu...")

# TAB
tab()

# ENTER
entrer()

# Flèche bas.
bas()

# ENTER
entrer()


# ============================================================
# ANNÉE
# ============================================================

print("Écriture de l'année...")

# TAB
tab()

# Écrit l'année.
taper(ANNEE)


# ============================================================
# VALIDATION DE LA DATE
# ============================================================

print("Validation de la date...")

# TAB
tab()

# ENTER
entrer()

# ENTER encore une fois.
entrer()


# ============================================================
# ÉTAPE SUIVANTE
# ============================================================

print()
print("Navigation vers l'étape suivante...")

# TAB
tab()

# TAB
tab()

# ENTER
entrer()


# ============================================================
# NOUVELLE PAGE
# ============================================================

print()
print("Nouvelle page...")

# TAB
tab()

# ENTER
entrer()


# ============================================================
# IDENTIFIANT
# ============================================================

print()
print("Navigation vers l'identifiant...")

# Flèche bas.
bas()

# Flèche bas.
bas()

print("Écriture de l'identifiant...")

# Écrit l'identifiant.
taper(IDENTIFIANT)


# ============================================================
# PAGE MOT DE PASSE
# ============================================================

print("Validation de l'identifiant...")

# ENTER
entrer()

print("Écriture du mot de passe...")

# Écrit le mot de passe.
taper(MOT_DE_PASSE)


# ============================================================
# VALIDATION DU MOT DE PASSE
# ============================================================

print("Validation du mot de passe...")

entrer()


# ============================================================
# CONFIRMATION DU MOT DE PASSE
# ============================================================

print()
print("Confirmation du mot de passe...")

# Réécrit le mot de passe.
taper(MOT_DE_PASSE)


# ============================================================
# VALIDATION
# ============================================================

print("Validation de la confirmation...")

entrer()


# ============================================================
# QR CODE
# ============================================================

print()
print("===================================")
print("       VÉRIFICATION QR CODE")
print("===================================")
print()

print("Le QR code devrait maintenant être affiché.")
print()
print("Valide le QR code manuellement avec ton téléphone.")
print()
print("Le programme attend automatiquement 2 min 30.")
print("Pendant ce temps, il n'envoie aucune touche.")
print()

# Attend 150 secondes = 2 minutes 30.
time.sleep(150)

print()
print("Les 150 secondes sont terminées.")
print("Reprise du test...")


# ============================================================
# APRÈS LES 150 SECONDES
# ============================================================

# ------------------------------------------------------------
# 1) TAB → ENTER
# ------------------------------------------------------------

print()
print("Étape après le QR code : 1")

tab()
entrer()


# ------------------------------------------------------------
# 2) TAB → TAB → TAB → ENTER
# ------------------------------------------------------------

print("Étape après le QR code : 2")

tab()
tab()
tab()
entrer()


# ------------------------------------------------------------
# 3) TAB → ENTER
# ------------------------------------------------------------

print("Étape après le QR code : 3")

tab()
entrer()


# ============================================================
# NOUVELLE PAGE
# ============================================================

print()
print("Nouvelle page...")

# TAB → ESPACE → TAB → ENTER
tab()
espace()
tab()
entrer()


# ============================================================
# NOUVELLE PAGE
# ============================================================

print()
print("Nouvelle page...")

# TAB → TAB → TAB → TAB → ENTER
tab()
tab()
tab()
tab()
entrer()


# ============================================================
# NOUVELLE PAGE
# ============================================================

print()
print("Nouvelle page...")

# TAB → TAB → TAB → ENTER
tab()
tab()
tab()
entrer()


# ============================================================
# NOUVELLE PAGE
# ============================================================

print()
print("Nouvelle page...")

# TAB → TAB → TAB → TAB → TAB → TAB → ENTER
tab()
tab()
tab()
tab()
tab()
tab()
entrer()


# ============================================================
# FIN DE LA SÉQUENCE
# ============================================================

print()
print("===================================")
print("   FIN DE LA SÉQUENCE ACTUELLE")
print("===================================")
print()

# Garde le terminal ouvert.
input("Appuie sur Entrée pour fermer le programme...")