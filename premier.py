# 1) améliorez ce code
# arrêt si diviseur * diviseur supérieur à n

# 2) modifiez le code
# Faire une fonction estPremier(n) qui rend True si n est premier, False sinon
# ATTENTION PAS DE PRINT DANS LA FONCTION !!!

# 3) enrichissez le code
# Appliquez succéssivement la fonction premier
# sur tous les nombres inférieurs ou égaux à 1000
# A rendre à pex.tellier@gmail.com


# 1) améliorez ce code
# arrêt si diviseur * diviseur supérieur à n

# 2) modifiez le code
# Faire une fonction estPremier(n) qui rend True si n est premier, False sinon
# ATTENTION PAS DE PRINT DANS LA FONCTION !!!

# 3) enrichissez le code
# Appliquez succéssivement la fonction premier
# sur tous les nombres inférieurs ou égaux à 1000

# A rendre à pex.tellier@gmail.com


def estpremier(n): #2 Fonction qui rend True si n est premier, False sinon
    for diviseur in range(2,n-1):
        if int(diviseur)**2 > n:    #1 arret si diviseur*diviseur>n pour tout les diviseurs
            raise Exception
            break

        else:
            if n%diviseur == 0:
                return False

            elif n%diviseur !=0:
                return True

print("Nombres premiers")
n = int(input("Entrez un nombre : "))
for i in range(1,n+1):

    # Application succéssivement la fonction premier
    # sur tous les nombres inférieurs ou égaux à input

        if estpremier(i):
            print("Le nombre", i, "est premier")
        elif estpremier(i) == False:
            print("Le nombre", i, "n'est pas premier")
        else:
            print("Le Diviseur fois diviseur est superieur du nombre",i," .")

