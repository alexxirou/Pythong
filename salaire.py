#renumeration minimum candidat pro:
#fonction age and diplome pour le taux de salaire par rapport au SMIC.
def f(a,d):
    if a<21 and d==1:
        t=(65/100)

    elif a<21 and d==2:
        t=(55/100)

    elif 21<a<26 and d==1:
        t=(80/100)

    elif 21<a<26 and d==2:
        t=(70/100)

    else:
        t=(80/100)

    return t

#input  variables age et diplome
age=int(input("Donnez le numero de l'age : "))
diplome=int(input("Choisissez le niveau d'education 1 pour BAC Pro ou 2 pour BAC: "))

taux=f(age,diplome)

print("Taux salaire est : "+str(taux)+ " de salaire base")