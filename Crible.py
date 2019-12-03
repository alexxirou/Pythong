def comparason(x):
    assert len(x)>=2 #affirmer que la liste a au moins deux elements
    Listresultat = []
    for i in range(0,len(x)-1):
        res=x[i]<=x[i+1]
        Listresultat.append(res)
    return Listresultat

def reorder(x):
    assert len(x) >= 2  # affirmer que la liste a au moins deux elements
    Listresultat = []
    for i in range(len(x)-1,-1,-1):
        Listresultat.append(x[i])
    return Listresultat

def bulle(x):
    assert len(x) >= 2  # affirmer que la liste a au moins deux elements
    for i in range(1,len(x)):
        if x[i]<x[i-1]:
            x[i-1],x[i]=x[i],x[i-1] # si derniere élément superieur de i inverser les positions dans la liste
    return x

l1=[]
designate=int(input("Number of items on first list:  ")) #créer une première liste  avec input de x elements
for i in range(0,designate):
    l1.append(input("Input number: "))

resultatcomparasons=comparason(l1)
print(resultatcomparasons)
resultatreorder=reorder(l1)
print(resultatreorder)
resultatbulle=bulle(l1)
print(sorted(l1))# evaluer que la dérniere valeur est la supériere
print(resultatbulle)
resultatbullen3=bulle(l1[:3])
print(resultatbullen3)
resultatdimbulle=bulledimin(l1)
print(resultatdimbulle)