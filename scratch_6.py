U=50000
q=0.96
for i in range(1,11):
    U=U*q
    S=U*(1-q**i)/(1-q)
    print("%.2f" % U,"%.2f"% S)