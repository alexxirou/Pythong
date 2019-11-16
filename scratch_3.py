def bonusmal(b):
    TA=100
    n=0
    while TA>50:
        TA=TA*(1-b)
        n=n+1
        print(n,TA)

bonusmal(0.05)