def inverseOf(nombre):
    listeDef=[]
    for i in range(2, nombre):
        print(nombre%i)
        if nombre%i>0:
            modc=i
            reste=nombre
            while reste%modc!=0 :
                resteb=modc
                #print("Reste is", resteb)
                modc=reste%modc
                #print("Modc is", modc)
                if modc==1:
                    listeDef.append(i)
                    break
                else:
                    reste=resteb         
    print(listeDef)

print(inverseOf(26))