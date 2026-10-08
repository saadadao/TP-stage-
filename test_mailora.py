from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://accounts.google.com/lifecycle/steps/signup/name?continue=https://accounts.google.com/&dsh=S-1240420547:1791384884293904&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://accounts.google.com/&TL=ADG-GRROH7xulSZm6QmQTNT_O5rRTPjTdZ2rB18jIju_FtXI-FafifKphg2ixmKu"

PRENOM = "Lucas"
NOM = "Martin"
JOUR = "15"
ANNEE = "2000"
MOT_DE_PASSE = "Test123456"


# Ouvre Chrome
navigateur = webdriver.Chrome()
navigateur.get(URL)

# Attend jusqu'à 15 secondes les éléments
attente = WebDriverWait(navigateur, 15)


# =========================
# PAGE 1 : prénom et nom
# =========================

prenom = attente.until(
    EC.element_to_be_clickable((By.ID, "firstName"))
)
prenom.send_keys(PRENOM)

nom = attente.until(
    EC.element_to_be_clickable((By.ID, "lastName"))
)
nom.send_keys(NOM)

suivant = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Suivant']")
    )
)
suivant.click()


# =========================
# PAGE 2 : date et genre
# =========================

jour = attente.until(
    EC.element_to_be_clickable((By.ID, "day"))
)
jour.send_keys(JOUR)

annee = attente.until(
    EC.element_to_be_clickable((By.ID, "year"))
)
annee.send_keys(ANNEE)


# Mois
menu_mois = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[normalize-space()='Mois']")
    )
)
menu_mois.click()

janvier = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//li[normalize-space()='Janvier']")
    )
)
janvier.click()


# Genre
menu_genre = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[normalize-space()='Genre']")
    )
)
menu_genre.click()

femme = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//li[normalize-space()='Femme']")
    )
)
femme.click()


suivant = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Suivant']")
    )
)
suivant.click()


# =========================
# PAGE 3 : adresse
# =========================

adresse_personnelle = attente.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[type='radio'][value='custom']")
    )
)
adresse_personnelle.click()


champs_adresse = attente.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    )
)

champ_adresse = None

for champ in champs_adresse:
    if champ.is_displayed():
        champ_adresse = champ
        break

if champ_adresse:
    champ_adresse.send_keys("lucas.martin.test")


suivant = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Suivant']")
    )
)
suivant.click()


# =========================
# PAGE 4 : mot de passe
# =========================

mot_de_passe = attente.until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "input[type='password']:not([name='PasswdAgain'])"
        )
    )
)
mot_de_passe.send_keys(MOT_DE_PASSE)


confirmation = attente.until(
    EC.element_to_be_clickable(
        (By.NAME, "PasswdAgain")
    )
)
confirmation.send_keys(MOT_DE_PASSE)


# Bouton final
suivant = attente.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Next']")
    )
)
suivant.click()


print("Test terminé !")
