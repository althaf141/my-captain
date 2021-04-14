x=int(input("enter the value of x :"))
n1,n2 = 0,1
sum=0
if x<=0:
    print("please enter the number greater than 0")
else:
    for i in range(0,x):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2
