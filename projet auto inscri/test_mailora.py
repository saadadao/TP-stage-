from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# =========================
# CONFIGURATION
# =========================

URL = "https://accounts.google.com/lifecycle/steps/signup/name?authuser=0&continue=https://myaccount.google.com/?utm_source%3Dsign_in_no_continue%26pli%3D1&dsh=S-182079701:1791447121138400&ec=GAlAwAE&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&rip=1&TL=ADG-GRQ_g3n58UhP_ZAOBreInFeXMoyxDhsfwJlymHvoQ6bnAv_epRjs7R78bzVn"

PRENOM = "Lucas"
NOM = "Durand"

JOUR = "5"
ANNEE = "2000"

IDENTIFIANT = "lucas.durand40771234"

MOT_DE_PASSE = "QAyziMlOggf"


# =========================
# NAVIGATEUR
# =========================

from selenium.webdriver.edge.options import Options

options = Options()
options.binary_location = "/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

navigateur = webdriver.Edge(options=options)
navigateur.get(URL)
attente = WebDriverWait(navigateur, 120)


# =========================
# PAUSE APRÈS CLIC
# =========================

def pause_clic():
    temps_random= random.uniform(2.5,17)
    time.sleep(temps_random)


# =========================
# CLIQUER SUR NEXT
# =========================

def cliquer_next():

    print("Recherche du bouton Next...")

    bouton = attente.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[.//span[@jsname='V67aGc' and "
                "(normalize-space()='Next' or "
                "normalize-space()='Suivant')]]"
            )
        )
    )

    bouton.click()
    pause_clic()

    print("Next cliqué.")


# =========================
# PREMIER NEXT
# =========================

print("Recherche du premier Next...")

premier_next = attente.until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "button[jsname='LgbsSe'][type='button']"
        )
    )
)

premier_next.click()
pause_clic()

print("Premier Next cliqué.")


# =========================
# PRÉNOM
# =========================

prenom = attente.until(
    EC.element_to_be_clickable(
        (By.ID, "firstName")
    )
)

prenom.click()
prenom.send_keys(PRENOM)

print("Prénom écrit.")


# =========================
# NOM
# =========================

nom = attente.until(
    EC.element_to_be_clickable(
        (By.ID, "lastName")
    )
)

nom.click()
nom.send_keys(NOM)

print("Nom écrit.")


# =========================
# NEXT
# =========================

cliquer_next()


# =========================
# JOUR
# =========================

jour = attente.until(
    EC.element_to_be_clickable(
        (By.ID, "day")
    )
)

jour.click()
jour.send_keys(JOUR)

print("Jour écrit.")


# =========================
# ANNÉE
# =========================

annee = attente.until(
    EC.element_to_be_clickable(
        (By.ID, "year")
    )
)

annee.click()
annee.send_keys(ANNEE)

print("Année écrite.")


# =========================
# MOIS
# =========================

menus = attente.until(
    EC.presence_of_all_elements_located(
        (
            By.CSS_SELECTOR,
            "div[jsname='oYxtQd'][role='combobox']"
        )
    )
)

menu_mois = menus[0]

menu_mois.click()
pause_clic()

print("Menu mois ouvert.")


fevrier = attente.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//li[@role='option']"
            "[.//span[normalize-space()='February']]"
        )
    )
)

navigateur.execute_script(
    "arguments[0].click();",
    fevrier
)

pause_clic()

print("Février sélectionné.")


# =========================
# GENRE
# =========================

menus = attente.until(
    EC.presence_of_all_elements_located(
        (
            By.CSS_SELECTOR,
            "div[jsname='oYxtQd'][role='combobox']"
        )
    )
)

menu_genre = menus[1]

menu_genre.click()
pause_clic()

print("Menu genre ouvert.")


female = attente.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//li[@role='option']"
            "[.//span[normalize-space()='Female']]"
        )
    )
)

navigateur.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    female
)

navigateur.execute_script(
    """
    arguments[0].dispatchEvent(
        new MouseEvent('mousedown', {
            bubbles: true,
            cancelable: true,
            view: window
        })
    );

    arguments[0].dispatchEvent(
        new MouseEvent('mouseup', {
            bubbles: true,
            cancelable: true,
            view: window
        })
    );

    arguments[0].click();
    """,
    female
)

pause_clic()

print("Female sélectionné.")


# =========================
# NEXT
# =========================

cliquer_next()


# =========================
# PAGE EMAIL
# =========================

print("Attente de la page email...")

attente.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//*[contains(normalize-space(), "
            "'Email address or phone number')]"
        )
    )
)

print("Page email détectée.")


# =========================
# 1 TAB + ENTER
# =========================

body = navigateur.find_element(By.TAG_NAME, "body")

print("Appui sur TAB...")
body.send_keys(Keys.TAB)
pause_clic()

# Récupère l'élément actuellement sélectionné par TAB
element_focus = navigateur.switch_to.active_element

print("Appui sur Entrée...")
element_focus.send_keys(Keys.ENTER)
pause_clic()

print("TAB + Entrée effectués.")


# =========================
# CHAMP IDENTIFIANT
# =========================

print("Recherche du champ identifiant...")

champs = attente.until(
    EC.presence_of_all_elements_located(
        (
            By.CSS_SELECTOR,
            "input.whsOnd.zHQkBf"
        )
    )
)

champ_identifiant = None

for champ in champs:

    if champ.is_displayed() and champ.is_enabled():

        champ_identifiant = champ
        break


if champ_identifiant is None:
    raise Exception(
        "ERREUR : champ identifiant introuvable."
    )


champ_identifiant.click()

champ_identifiant.send_keys(
    IDENTIFIANT
)

print("Identifiant écrit :", IDENTIFIANT)


# =========================
# NEXT
# =========================

cliquer_next()


# =========================
# MOT DE PASSE
# =========================

print("Recherche du mot de passe...")

mot_de_passe = attente.until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "input[type='password']:not([name='PasswdAgain'])"
        )
    )
)

mot_de_passe.click()

mot_de_passe.send_keys(
    MOT_DE_PASSE
)

print("Mot de passe écrit.")


# =========================
# CONFIRMATION
# =========================

confirmation = attente.until(
    EC.element_to_be_clickable(
        (By.NAME, "PasswdAgain")
    )
)

confirmation.click()

confirmation.send_keys(
    MOT_DE_PASSE
)

print("Confirmation écrite.")


# =========================
# DERNIER NEXT
# =========================

cliquer_next()


# =========================
# FIN
# =========================

print()
print("==============================")
print("       TEST TERMINÉ")
print("==============================")
print()

input(
    "Appuie sur Entrée pour fermer le navigateur..."
)

navigateur.quit()