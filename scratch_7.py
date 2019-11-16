U0 = 5
U1=13/6
for i in range(2,6):
    U2=((5/6)*U1) - ((1/6)*U0)
    print(i, U2)
    U0=U1
    U1=U2
