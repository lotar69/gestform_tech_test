import random

n = random.randint(-1000,1000)

if n % 3 == 0 and n % 5 == 0:
    print("Gestform")
elif n % 3 == 0:
    print("Geste")
elif n % 5 == 0:
    print("Forme")
else:
    print(n)