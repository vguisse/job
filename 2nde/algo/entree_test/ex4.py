from random import randint

de = randint(1,6)
print(de)

secret = randint(0,1000)
for essai in range(10):
    print("Devinez mon nombre secret :")
    nombreSaisi = int(input())
    if nombreSaisi == secret:
        print("Bravo, vous êtes perspicace.")
        break
    else:
        print("Et non, bien tenté.")

