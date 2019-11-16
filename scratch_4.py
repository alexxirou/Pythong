i= int(input("Please input interest rate"))/100
n=0
C=10000
while C<20000:
    n=n+1
    C=(1+i)*C
    print(n,C)