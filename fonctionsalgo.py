def bis(a):
    if a%4==0 and a%400==0 and a%100==0:
        res=True
    else:
        res=False
    return res

def nbjours(m,a):
    if m in (1,3,5,7,8,10,12):
        res=31
    elif m==2 and bis(a):
        res=29
    elif m==2 and bis(a)==False:
        res=28
    elif m in (4,6,9,12):
        res=30
    else:
        res=False

    return res

def quant(j,m,a):
    if m==1:
        res=j
    elif m=2:
        res=31+j
    return res

an=int(input("Anneé?"))
mois=int(input("Mois?"))
jour=int(input("Jour?"))
v=quant(jour,mois,an)
print(v)



