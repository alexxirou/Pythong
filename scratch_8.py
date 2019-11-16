def emission(p,q,n):
    while p>100:
        n=n+1
        p=(q)*p

    return n

n=0
q=0.883
p=635.0

an=emission(635.0,0.883,0)
print(an)