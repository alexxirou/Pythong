import statistics

data=[]
li=int(input("Input the total number of items: "))
for i in range(0,li):
    data.append(int(input("Input number "+str(i+1)+": ")))

x=statistics.mean(data)

print("The mean of the data is: "+str(x))