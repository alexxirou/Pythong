import numpy as np
import re

def equationToMatrix(*args):
    listeres=[]
    A=[]
    B=[]
    pattern = r'([=])'
    for arg in args:
        res=re.split(pattern,arg)
        liste1=list(map(int, re.findall(r'-?\d+', res[0])))
        liste2=list(map(int,re.findall(r'-?\d+', res[2])))
        A.append(liste1)
       
        B.append(liste2)
       

    A=np.array(A)
    
    B=np.array(B)
    
    try: 
        inv=np.linalg.inv(A)
        res=inv.dot(B)
    except np.linalg.LinAlgError:
        print("Pas de solution")
    return res
        
    



matrices=(equationToMatrix("1x+6y=15","2x-4y=45"))



for i in range(0,len(matrices)):
    print("La variable numéro", i+1, "est:",matrices[i])
