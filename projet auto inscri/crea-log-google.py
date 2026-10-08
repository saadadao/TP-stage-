# ============================================================
# PROGRAMME : Générateur de données fictives
# ============================================================
#
# Ce programme sert à créer des données de test fictives.
#
# Il génère :
#   - un prénom
#   - un nom
#   - un mot de passe aléatoire
#   - un identifiant fictif
#
# Le programme crée 40 lignes et les met dans un tableau.
#
# IMPORTANT :
# Toutes les informations générées sont fictives.
# Elles ne servent pas à créer de vrais comptes.
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTER LES LIBRAIRIES
# ------------------------------------------------------------

# "random" permet de choisir des éléments au hasard.
import random

# "string" contient des caractères déjà préparés :
# lettres, chiffres, etc.
import string

# "csv" permet de créer un fichier contenant notre tableau.
import csv


# ------------------------------------------------------------
# 2. LISTE DES PRÉNOMS
# ------------------------------------------------------------

# Cette liste contient des prénoms fictifs que le programme
# pourra choisir aléatoirement.
prenoms = [
    "Lucas",
    "Noah",
    "Hugo",
    "Léo",
    "Nathan",
    "Louis",
    "Ethan",
    "Tom",
    "Arthur",
    "Gabriel",
    "Jules",
    "Adam",
    "Maxime",
    "Théo",
    "Enzo",
    "Mathis",
    "Sacha",
    "Paul",
    "Alexis",
    "Nolan"
]


# ------------------------------------------------------------
# 3. LISTE DES NOMS
# ------------------------------------------------------------

# Même principe que pour les prénoms.
# Le programme choisira un nom au hasard dans cette liste.
noms = [
    "Martin",
    "Bernard",
    "Dubois",
    "Thomas",
    "Robert",
    "Richard",
    "Petit",
    "Durand",
    "Leroy",
    "Moreau",
    "Simon",
    "Laurent",
    "Lefebvre",
    "Michel",
    "Garcia",
    "David",
    "Bertrand",
    "Roux",
    "Vincent",
    "Fournier"
]


# ------------------------------------------------------------
# 4. FONCTION POUR CRÉER UN MOT DE PASSE
# ------------------------------------------------------------

def generer_mot_de_passe():
    # Cette fonction sert à fabriquer un mot de passe aléatoire.

    # On crée une liste contenant :
    # - les lettres minuscules
    # - les lettres majuscules
    # - les chiffres
    # - certains caractères spéciaux
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"

    # "random.choice()" choisit un caractère au hasard.
    #
    # On répète cette opération 12 fois.
    #
    # "join()" permet ensuite de réunir tous les caractères
    # pour former un seul mot de passe.
    mot_de_passe = "".join(
        random.choice(caracteres)
        for _ in range(12)
    )

    # "return" permet de renvoyer le mot de passe
    # à l'endroit où la fonction a été appelée.
    return mot_de_passe


# ------------------------------------------------------------
# 5. FONCTION POUR CRÉER UN IDENTIFIANT FICTIF
# ------------------------------------------------------------

def generer_id(prenom, nom):
    # Cette fonction reçoit le prénom et le nom.

    # On choisit un nombre aléatoire entre 1000 et 9999.
    nombre = random.randint(1000, 9999)

    # On construit l'identifiant avec :
    # prénom + nom + nombre.
    #
    # ".lower()" transforme les lettres en minuscules.
    identifiant = (
        prenom.lower()
        + "."
        + nom.lower()
        + str(nombre)
    )

    # On renvoie l'identifiant créé.
    return identifiant


# ------------------------------------------------------------
# 6. CRÉATION DU TABLEAU
# ------------------------------------------------------------

# Cette liste va contenir toutes les personnes générées.
tableau = []


# ------------------------------------------------------------
# 7. CRÉER 40 LIGNES
# ------------------------------------------------------------

# "range(40)" permet de répéter le programme 40 fois.
for i in range(40):

    # On choisit un prénom au hasard.
    prenom = random.choice(prenoms)

    # On choisit un nom au hasard.
    nom = random.choice(noms)

    # On génère un mot de passe aléatoire.
    mot_de_passe = generer_mot_de_passe()

    # On génère un identifiant fictif.
    identifiant = generer_id(prenom, nom)

    # On crée une ligne sous forme de dictionnaire.
    #
    # Un dictionnaire fonctionne avec :
    # "nom_de_la_colonne": valeur
    ligne = {
        "Prenom": prenom,
        "Nom": nom,
        "Mot de passe": mot_de_passe,
        "Identifiant": identifiant
    }

    # On ajoute cette ligne dans notre tableau.
    tableau.append(ligne)


# ------------------------------------------------------------
# 8. AFFICHER LE TABLEAU DANS LA CONSOLE
# ------------------------------------------------------------

print("\n" + "=" * 80)

# Titre du tableau.
print("                DONNEES FICTIVES")

print("=" * 80)

# On affiche les titres des colonnes.
print(
    f"{'N°':<5}"
    f"{'Prenom':<15}"
    f"{'Nom':<15}"
    f"{'Mot de passe':<20}"
    f"{'Identifiant':<25}"
)

print("-" * 80)


# On parcourt chaque ligne du tableau.
for numero, personne in enumerate(tableau, start=1):

    # On affiche les informations de chaque personne.
    print(
        f"{numero:<5}"
        f"{personne['Prenom']:<15}"
        f"{personne['Nom']:<15}"
        f"{personne['Mot de passe']:<20}"
        f"{personne['Identifiant']:<25}"
    )


# ------------------------------------------------------------
# 9. CRÉER UN FICHIER CSV
# ------------------------------------------------------------

# "open()" permet d'ouvrir ou de créer un fichier.
#
# "w" signifie "write" :
# on veut écrire dans le fichier.
#
# "newline=''" évite d'avoir des lignes vides
# supplémentaires dans certains systèmes.
with open(
    "donnees_fictives.csv",
    "w",
    newline="",
    encoding="utf-8"
) as fichier:

    # On indique quelles sont les colonnes du tableau.
    colonnes = [
        "Prenom",
        "Nom",
        "Mot de passe",
        "Identifiant"
    ]

    # DictWriter permet d'écrire nos dictionnaires
    # directement dans le fichier CSV.
    ecrivain = csv.DictWriter(
        fichier,
        fieldnames=colonnes
    )

    # Cette ligne écrit la première ligne du fichier :
    # Prenom | Nom | Mot de passe | Identifiant
    ecrivain.writeheader()

    # Cette ligne écrit toutes les personnes générées.
    ecrivain.writerows(tableau)


# ------------------------------------------------------------
# 10. MESSAGE FINAL
# ------------------------------------------------------------

print("\n" + "=" * 80)

# On indique que le programme est terminé.
print("40 personnes fictives ont été générées.")

# On indique où se trouve le tableau.
print("Le tableau a été enregistré dans : donnees_fictives.csv")

print("=" * 80)