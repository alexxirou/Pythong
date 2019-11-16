#exercice sur les suites d'une entreprise
#A
#a
    #la nature de la suite a(n) des depenses de la service A est arithmetique avec une raison de 4000 pour les 4 premier elements
#a2-a1=a3-a2=a4-a3=4000

#b
def serviceA(n):
    a1=20000
    r=4000
    for i in range(1,n+1):
        an=a1+((n)*r)
    return an

#c
a10=serviceA(10)
print(a10)

#2
def somme(n):
    a1=20000
    r=4000
    for i in range (1,n+1):
        somme=(n+1)*(a1+r)/2
    return somme

#3
R10=somme(10)
print(R10) #somme des depenses de la service A pour 10 ans


#B

#1
b1=20000
r=1.15
b2=b1*(r)
b3=b2*(r)
b4=b3*(r)

#2 Service B est une suite géométrique avec raison =1.15.
    #bn=20000*((1.15)**n)

#3
b2=20000*((1.15)**2)
print(round(b2))

#C comparaison des services
n=10
a1=b1
r1=4000
r2=1.15
a10=a1+(n*r1)
b10=b1*(r2**n)
if a10>b10:
    print("a10"+" = "+str(a10)+" > "+"b10"+" = "+str(b10))
elif a10<b10:
    print("a10"+" = "+str(a10)+" < "+"b10"+" = "+str(b10))
else:
    print("a10==b10"+"="+a10)