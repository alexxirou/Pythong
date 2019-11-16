#Deviner un nombre aléatoire.
from random import*

randomnumber=randint(1,1000)

for i in range(9):
    guess=int(input("Choose a number:" ))
    if (guess == randomnumber):
        print("Correct!")
        break
    else:
        print("Try again... tries remaining: "+str(9-i))

print("Game over")






