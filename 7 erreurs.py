def difference(list1,list2):
    Listresultat=[]
    assert len(list1)==len(list2) #verfier la taille de la liste
    for e in range(0,len(list1)): # pour chaque element de list1 comparer avec l' element de list2 dans la meme position
        res=list1[e]==list2[e]
        Listresultat.append(res)
    return Listresultat

l1=[]
x=int(input("Number of items on first list:  ")) #créer une première liste  avec input de x elements
for i in range(0,x):
    l1.append(input("Input number: "))
l2=[]
y=int(input("Number of items on second list:  ")) #créer une  deuxième liste avec input de y elements
for i in range (0,y):
    l2.append(input("Input number: "))
result=difference(l1,l2)
print(result)