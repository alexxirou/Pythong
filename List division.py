
def cut(x): #division d'une liste par la position
    y=[]
    z=[]
    for element in range(0,len(x)):
        if element%2==0:
            y.append(x[element])
        else:
            z.append(x[element])
    return y,z

c=([4,6,0,5,9,0,0,3])
res=cut(c)
print(res)