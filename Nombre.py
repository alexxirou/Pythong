#TP algo
#exercise no,bre pair

#fonction pair
def pair(n):
    reste=n%2
    if reste==0:
        res=True

    else:
        res=False
    return res
#input
na=int(input("Donnez le nombre: " ))
p=pair(na)

if p:
    print("Le nombre "+str(na)+" est pair.")
else:
    print("Le nombre "+str(na)+ " est unpair.")

