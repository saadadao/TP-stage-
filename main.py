import re

def score(mdp):
    point = 0

    if len(mdp) >= 12:
        point += 25

    if re.search(r"(.*[A-Z]){2}", mdp):
        point += 25

    if re.search(r"(.*\d){4}", mdp):
        point += 25

    if re.search(r"[^\w\s]", mdp):
        point += 25

    return point


mot = input("Enter your password : ")

s = score(mot)

print(f"Score : {s}/100")
