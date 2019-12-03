def eratosthene(x):
    emptylist=[]
    startlist=list(range(0,x))
    for variable in range(2,x): # boucle pour prendre tous les variables de 2 jusqu'a x
        for i in range(2*variable,x,variable): #boucle pour trouver les multiples de variable commencant à 2*v
            startlist[i]=-1
    for e in startlist[2:]: #boucle pour ajouter les primaires dans un nouveau list
        if e != -1:
            emptylist.append(e)
    if emptylist[-1]==x:
        res=str(x)+" est primaire"
    else:
        res=str(x)+" n'est pas primaire"

    return emptylist, res

print(2,3,5,7,11,13,17,19 )# test for results
print(eratosthene(20))