import re

def subnetCalc(ipAdresse):
    pattern = r'([/])'
    liste=re.split(pattern,ipAdresse)#separer l'input avec le délimiter "/"
    ip=list(map(int, re.findall(r'\d+', liste[0] )))#regex pour garder les nombres du string comme intergers
    sub=int(liste[2])
    subnetmask=[] 
    invmask=[]
    reseau=[]
    phost=[]
    lhost=[]
    i=0
    while sub>=8: #division de bits reseau aux octets
        sub=sub-8
        subnetmask.append((2**8)-1)#calcul de la masque réseau 
        i+=1
    subnetmask.append(256-(2**(8-sub))) #pour ajouter les bits qui restent au dernier octet 
    while len(subnetmask)<4:
        subnetmask.append(0) #addition d'un 0 au dernier octer si les octets remplis sont moins de 4
    #print(subnetmask)
    listebin=ip
    for i in range(0,4):
        invmask.append(255-subnetmask[i])#caculation de la masque inversée 
        bitreseau=(listebin[i] & subnetmask[i]) #calculation des octets d' ip reseau (op. bin. "and")
        bitbroadcast=(listebin[i] | invmask[i])#calculationde des octets d' ip broadcast (op. bin "or")
        reseau.append(bitreseau)
        phost.append(bitreseau)
        lhost.append(bitbroadcast)
    phost[3]+=1 #addition d'un bit au dernier octet d'ip reseau pour trouver la première adresse hôte
    lhost[3]-=1 #soustraction d'un bit du dernier octet d'ip broadcast pour trouver la dernière adresse hôte

    return reseau,phost,lhost
      
    
res=subnetCalc("192.168.10.0/15")
print("L'adresse reseau est:", res[0])
print("L'adresse du premier hôte est:", res[1])
print("L'adresse du dernier hôte est;", res[2])
