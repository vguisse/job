# Code à améliorer avec une fonction.
for i in range(5):
    print("/\  ", end="")
print()
for i in range(5):
    print("  \/", end="")
print()
print("     Une vague.")
print()
for i in range(4):
    for i in range(5):
        print("/\  ", end="")
    print()
    for i in range(5):
        print("  \/", end="")
    print()
print("       La mer.")

# Code amélioré
def vague():
    for i in range(5):
        print("/\  ", end="")
    print()
    for i in range(5):
        print("  \/", end="")
    print()
    
vague()
print("     Une vague.")
print()
for i in range(4):
    vague()
print("       La mer.")
