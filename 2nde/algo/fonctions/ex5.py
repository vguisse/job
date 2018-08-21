# code à tester
def valeurAbsolue(x):
    if x >= 0:
        return x
    else:
        return -x

print("Saisissez un nombre :")
texteSaisi = input()
a = int(texteSaisi)
b = valeurAbsolue(a)
print("Vous avez saisi le nombre : ", a)
print("Sa valeur absolue est : ", b)

# code à compléter
def somme(n):
    s = 0
    cpt = 1
    for i in range(n):
        s = s + cpt
        cpt = cpt + 1
    return s

print("Saisissez un nombre entier :")
texteSaisi = input()
a = int(texteSaisi)
b = somme(a)
print("La somme des entiers jusqu'à ", a, "vaut ", b)