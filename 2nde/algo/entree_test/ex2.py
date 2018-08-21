secret = 42
print("Devinez mon nombre secret :")
nombreSaisi = int(input())
if nombreSaisi == secret:
    print("Bravo, vous êtes perspicace.")
else:
    print("Et non, bien tenté.")
