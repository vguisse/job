def ligneEtoilee(longueur):
    for i in range(longueur):
        print("*", end="")
    print()


def box(texte):
    ligneCentrale = "* " + texte + " *"
    l = len(ligneCentrale)
    ligneEtoilee(l)
    print(ligneCentrale)
    ligneEtoilee(l)