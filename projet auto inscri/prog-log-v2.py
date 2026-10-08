import pyautogui
import time


# ============================================================
# CONFIGURATION
# ============================================================

URL = "TON_URL_DE_TEST"

PRENOM = "Lucas"
NOM = "Martin"
JOUR = "5"
ANNEE = "2000"
IDENTIFIANT = "lucas.martin.test12342441"
MOT_DE_PASSE = "Test123456"


# ============================================================
# FONCTIONS
# ============================================================

def pause():
    """Attend 1 seconde."""
    time.sleep(1)


def taper(texte):
    """Écrit le texte lettre par lettre."""
    pyautogui.write(texte, interval=0.1)


def tab():
    """Appuie sur TAB puis attend 1 seconde."""
    pyautogui.press("tab")
    pause()


def entrer():
    """Appuie sur ENTRÉE puis attend 1 seconde."""
    pyautogui.press("enter")
    pause()


# ============================================================
# LANCEMENT
# ============================================================

print("Le programme va commencer dans 3 secondes...")
time.sleep(3)

# Ouvre Edge Windows avec l'URL de test
pyautogui.hotkey("win", "r")
pause()

pyautogui.write("msedge " + URL, interval=0.03)
pyautogui.press("enter")

print("Edge lancé.")
print("Attente du chargement...")
time.sleep(5)


# ============================================================
# PREMIÈRE PAGE
# ============================================================

print("Navigation dans la page...")

entrer()


# ============================================================
# PRÉNOM
# ============================================================

print("Écriture du prénom...")

taper(PRENOM)
tab()


# ============================================================
# NOM
# ============================================================

print("Écriture du nom...")

taper(NOM)
tab()


# ============================================================
# PASSER À L'ÉTAPE SUIVANTE
# ============================================================

print("Validation...")

entrer()


# ============================================================
# DATE
# ============================================================

print("Écriture du jour...")

taper(JOUR)
tab()

print("Écriture de l'année...")

taper(ANNEE)
tab()


# ============================================================
# MOIS
# ============================================================

print("Sélection du mois...")

entrer()
pause()

# À adapter selon le nombre de touches nécessaires
# tab()
# tab()
# entrer()


# ============================================================
# GENRE
# ============================================================

print("Sélection du genre...")

tab()
entrer()


# ============================================================
# PAGE SUIVANTE
# ============================================================

print("Passage à l'étape suivante...")

entrer()

print("Attente de la page suivante...")
time.sleep(3)


# ============================================================
# PAGE EMAIL / IDENTIFIANT
# ============================================================

print("Navigation vers l'identifiant...")

# 1 TAB → 1 seconde → ENTER → 1 seconde
tab()
entrer()


# ============================================================
# IDENTIFIANT
# ============================================================

print("Écriture de l'identifiant...")

taper(IDENTIFIANT)
tab()


# ============================================================
# MOT DE PASSE
# ============================================================

print("Écriture du mot de passe...")

taper(MOT_DE_PASSE)
tab()


# ============================================================
# CONFIRMATION DU MOT DE PASSE
# ============================================================

print("Confirmation du mot de passe...")

taper(MOT_DE_PASSE)
tab()


# ============================================================
# VALIDATION FINALE
# ============================================================

print("Validation finale...")

entrer()

print()
print("===================================")
print("TEST TERMINÉ")
print("===================================")

input("Appuie sur Entrée pour fermer le programme...")