from random import randint

secret = randint(1,100)
for i in range(10) :
    print("devinez mon nombre secret :")
    nombreSaisi = int(input())
    if nombreSaisi == secret :
        print("Bravo, vous êtes perspicase.")
        break
    else :
        print("Et non, bien tenté.")
        if nombreSaisi < secret :
            print("Trop petit")
        else :
            print("Trop grand")
nbEssai = i + 1
print("tu as réussi au bout de l'essai numéro",nbEssai)
if nbEssai < 2 :
    print("Tu triche c'est ça ???")
else :
    if nbEssai < 5 :
        print("Jolie")
    else :
        if nbEssai < 8 :
            print("Tu te débrouille plutôt bien !!!")
        else :
            print("Tu es capable de mieux quand même")


