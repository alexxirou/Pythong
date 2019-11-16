#Application du barème des impôts:
#function pour QF 0 à 9964 euro
def taux1(x):
    if x<=9964:
        res=0
#Qf de 9964 à 27519 euro
    elif 9964<x<=27519:
        res=(x-9964)*0.14
#Qf de 27519 à 73779 euro
    elif 27519<x<=73779:
        res=((x-27519)*0.3)+((27519-9964)*0.14)
#QF de 73779 à 156244 euro
    elif 73779<x<=156244:
        res=(((x-73779)*0.41)+((73779-27519)*0.3)+((27519-9964)*0.14))
#QF de 156244....
    elif 156244<x:
        res=(((x-156244)*0.45)+((156244-73779)*0.41)+((73779-27519)*0.3)+((27519-9964)*0.14))
    return res

#input QF

QF=int(input("Saisissez le tailleur du Quatient Familial (numéro sans espaces) : "))
Impots=taux1(QF)
print("Les impôts à payer sont : "+str(Impots)+" €."   )