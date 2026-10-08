# ============================================================
# GÉNÉRATEUR DE DONNÉES FICTIVES
# ============================================================
#
# Ce programme crée une petite interface graphique permettant
# de générer des données fictives pour un projet de simulation.
#
# Le programme peut générer :
#   - un prénom
#   - un nom
#   - un mot de passe aléatoire
#   - un identifiant fictif
#
# Les données sont affichées dans un tableau.
#
# IMPORTANT :
# Ces données sont uniquement fictives et destinées à des tests.
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTER LES LIBRAIRIES
# ------------------------------------------------------------

# tkinter permet de créer des fenêtres, boutons,
# champs de texte et tableaux.
import tkinter as tk

# ttk contient des éléments graphiques supplémentaires,
# notamment le tableau Treeview.
from tkinter import ttk

# messagebox permet d'afficher des petites fenêtres
# avec des messages d'erreur ou d'information.
from tkinter import messagebox

# csv permet de créer un fichier CSV.
import csv

# random permet de choisir des éléments au hasard.
import random

# string contient des lettres et des chiffres prêts à utiliser.
import string


# ------------------------------------------------------------
# 2. LISTES DE PRÉNOMS ET DE NOMS
# ------------------------------------------------------------

# Liste de prénoms que le programme peut utiliser.
prenoms = [
    "Lucas", "Noah", "Hugo", "Leo", "Nathan",
    "Louis", "Ethan", "Tom", "Arthur", "Gabriel",
    "Jules", "Adam", "Maxime", "Theo", "Enzo",
    "Mathis", "Sacha", "Paul", "Alexis", "Nolan"
]

# Liste de noms que le programme peut utiliser.
noms = [
    "Martin", "Bernard", "Dubois", "Thomas", "Robert",
    "Richard", "Petit", "Durand", "Leroy", "Moreau",
    "Simon", "Laurent", "Lefebvre", "Michel", "Garcia",
    "David", "Bertrand", "Roux", "Vincent", "Fournier"
]


# ------------------------------------------------------------
# 3. FONCTION POUR CRÉER UN MOT DE PASSE
# ------------------------------------------------------------

def generer_mot_de_passe():

    # On rassemble les lettres minuscules, majuscules,
    # les chiffres et quelques caractères spéciaux.
    caracteres = (
        string.ascii_letters
        + string.digits
        + "!@#$%&*"
    )

    # On choisit 12 caractères au hasard.
    mot_de_passe = "".join(
        random.choice(caracteres)
        for _ in range(12)
    )

    # On renvoie le mot de passe.
    return mot_de_passe


# ------------------------------------------------------------
# 4. FONCTION POUR CRÉER UN IDENTIFIANT
# ------------------------------------------------------------

def generer_id(prenom, nom):

    # On choisit un nombre aléatoire entre 1000 et 9999.
    nombre = random.randint(1000, 9999)

    # On construit l'identifiant.
    identifiant = (
        prenom.lower()
        + "."
        + nom.lower()
        + str(nombre)
    )

    # On renvoie l'identifiant.
    return identifiant


# ------------------------------------------------------------
# 5. FONCTION QUI GÉNÈRE LES PERSONNES
# ------------------------------------------------------------

def generer_personnes():

    # On récupère ce qui est écrit dans le champ
    # où l'utilisateur indique le nombre de personnes.
    texte_nombre = champ_nombre.get()

    # On vérifie que l'utilisateur a bien écrit quelque chose.
    if texte_nombre == "":
        messagebox.showerror(
            "Erreur",
            "Entre un nombre de personnes."
        )
        return

    # On essaie de transformer le texte en nombre entier.
    try:
        nombre = int(texte_nombre)

    # Si la conversion échoue, ce bloc est exécuté.
    except ValueError:
        messagebox.showerror(
            "Erreur",
            "Entre uniquement un nombre."
        )
        return

    # On empêche l'utilisateur d'entrer un nombre négatif
    # ou zéro.
    if nombre <= 0:
        messagebox.showerror(
            "Erreur",
            "Le nombre doit être supérieur à 0."
        )
        return

    # On limite le nombre pour éviter de générer
    # accidentellement énormément de lignes.
    if nombre > 500:
        messagebox.showerror(
            "Erreur",
            "Maximum : 500 personnes."
        )
        return

    # On supprime les anciennes lignes du tableau.
    for ligne in tableau.get_children():
        tableau.delete(ligne)

    # On répète la génération autant de fois
    # que le nombre demandé.
    for numero in range(1, nombre + 1):

        # Choix aléatoire du prénom.
        prenom = random.choice(prenoms)

        # Choix aléatoire du nom.
        nom = random.choice(noms)

        # Création du mot de passe.
        mot_de_passe = generer_mot_de_passe()

        # Création de l'identifiant.
        identifiant = generer_id(prenom, nom)

        # On ajoute les informations dans le tableau.
        tableau.insert(
            "",
            "end",
            values=(
                numero,
                prenom,
                nom,
                mot_de_passe,
                identifiant
            )
        )


# ------------------------------------------------------------
# 6. FONCTION POUR EFFACER LE TABLEAU
# ------------------------------------------------------------

def effacer_tableau():

    # On parcourt toutes les lignes présentes.
    for ligne in tableau.get_children():

        # On supprime chaque ligne.
        tableau.delete(ligne)


# ------------------------------------------------------------
# 7. FONCTION POUR EXPORTER LE TABLEAU
# ------------------------------------------------------------

def exporter_csv():

    # On récupère toutes les lignes présentes dans le tableau.
    lignes = tableau.get_children()

    # S'il n'y a aucune ligne, on affiche une erreur.
    if not lignes:
        messagebox.showerror(
            "Erreur",
            "Il n'y a aucune donnée à exporter."
        )
        return

    # On crée le fichier CSV.
    with open(
        "donnees_fictives.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as fichier:

        # Création de l'écrivain CSV.
        ecrivain = csv.writer(fichier)

        # Première ligne : les noms des colonnes.
        ecrivain.writerow([
            "Numero",
            "Prenom",
            "Nom",
            "Mot de passe",
            "Identifiant"
        ])

        # On récupère chaque ligne du tableau.
        for ligne in lignes:

            # "item()" récupère les informations
            # contenues dans cette ligne.
            valeurs = tableau.item(ligne)["values"]

            # On écrit la ligne dans le fichier CSV.
            ecrivain.writerow(valeurs)

    # Message indiquant que l'export est terminé.
    messagebox.showinfo(
        "Terminé",
        "Le fichier donnees_fictives.csv a été créé."
    )


# ============================================================
# 8. CRÉATION DE LA FENÊTRE
# ============================================================

# On crée la fenêtre principale.
fenetre = tk.Tk()

# Titre affiché en haut de la fenêtre.
fenetre.title("Générateur de données fictives")

# Taille initiale de la fenêtre.
fenetre.geometry("900x550")


# ------------------------------------------------------------
# 9. TITRE
# ------------------------------------------------------------

# Création d'un texte pour le titre.
titre = tk.Label(
    fenetre,
    text="Générateur de données fictives",
    font=("Arial", 20, "bold")
)

# "pack()" permet de placer l'élément dans la fenêtre.
titre.pack(pady=15)


# ------------------------------------------------------------
# 10. ZONE POUR LE NOMBRE DE PERSONNES
# ------------------------------------------------------------

# Création d'un petit texte explicatif.
label_nombre = tk.Label(
    fenetre,
    text="Nombre de personnes à générer :"
)

label_nombre.pack()


# Création du champ dans lequel l'utilisateur
# pourra écrire un nombre.
champ_nombre = tk.Entry(
    fenetre,
    width=20
)

champ_nombre.pack(pady=5)

# On met 40 directement dans le champ au démarrage.
champ_nombre.insert(0, "40")


# ------------------------------------------------------------
# 11. ZONE DES BOUTONS
# ------------------------------------------------------------

# Frame = une petite zone permettant de regrouper
# plusieurs éléments graphiques.
zone_boutons = tk.Frame(fenetre)

zone_boutons.pack(pady=10)


# Bouton pour générer les données.
bouton_generer = tk.Button(
    zone_boutons,
    text="Générer",
    command=generer_personnes,
    width=15
)

bouton_generer.grid(
    row=0,
    column=0,
    padx=5
)


# Bouton pour effacer le tableau.
bouton_effacer = tk.Button(
    zone_boutons,
    text="Effacer",
    command=effacer_tableau,
    width=15
)

bouton_effacer.grid(
    row=0,
    column=1,
    padx=5
)


# Bouton pour exporter les données.
bouton_exporter = tk.Button(
    zone_boutons,
    text="Exporter CSV",
    command=exporter_csv,
    width=15
)

bouton_exporter.grid(
    row=0,
    column=2,
    padx=5
)


# ------------------------------------------------------------
# 12. CRÉATION DU TABLEAU
# ------------------------------------------------------------

# Liste des colonnes du tableau.
colonnes = (
    "numero",
    "prenom",
    "nom",
    "mot_de_passe",
    "identifiant"
)


# Création du tableau.
tableau = ttk.Treeview(
    fenetre,
    columns=colonnes,
    show="headings"
)


# ------------------------------------------------------------
# 13. NOMS DES COLONNES
# ------------------------------------------------------------

# Texte affiché au-dessus de chaque colonne.

tableau.heading(
    "numero",
    text="N°"
)

tableau.heading(
    "prenom",
    text="Prénom"
)

tableau.heading(
    "nom",
    text="Nom"
)

tableau.heading(
    "mot_de_passe",
    text="Mot de passe"
)

tableau.heading(
    "identifiant",
    text="Identifiant"
)


# ------------------------------------------------------------
# 14. LARGEUR DES COLONNES
# ------------------------------------------------------------

tableau.column(
    "numero",
    width=50
)

tableau.column(
    "prenom",
    width=150
)

tableau.column(
    "nom",
    width=150
)

tableau.column(
    "mot_de_passe",
    width=220
)

tableau.column(
    "identifiant",
    width=250
)


# On affiche le tableau.
tableau.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


# ------------------------------------------------------------
# 15. LANCEMENT DU PROGRAMME
# ------------------------------------------------------------

# Cette ligne démarre la fenêtre.
#
# Tant que la fenêtre est ouverte, Python attend les actions
# de l'utilisateur : clic sur les boutons, écriture, etc.
fenetre.mainloop()