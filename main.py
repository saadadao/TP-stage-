import re

def score(mdp):
    longueur = len(mdp) >= 12
    majuscules = bool(re.search(r"(.*[A-Z]){2}", mdp))
    chiffres = bool(re.search(r"(.*\d){4}", mdp))
    special = bool(re.search(r"[^\w\s]", mdp))

    print("12 caractères minimum :", longueur)
    print("2 majuscules          :", majuscules)
    print("4 chiffres            :", chiffres)
    print("1 caractère spécial   :", special)
    
    if longueur == False:
        print("Nombre de caractères insuffisant")
    if majuscules == False:
        print("Nombre de Majuscules insuffisant")
    if chiffres == False:
        print("Nombre de chiffres insuffisant")
    if special == False:
        print("Nombre de caractères spéciaux insuffisant")

    point = 0
    if longueur:
        point += 25
    if majuscules:
        point += 25
    if chiffres:
        point += 25
    if special:
        point += 25
    return point

while True :
    mot = input("Mot de passe (q pour quitter) : ")
    if mot == "q":
        break 
    s = score(mot)


    critères_valide = s // 25  

    if critères_valide <= 1:
        print("score : Faible")
    elif critères_valide <= 3:
        print("Moyen")
    else:
        print("Fort")

    print(f"Score : {s}/100")