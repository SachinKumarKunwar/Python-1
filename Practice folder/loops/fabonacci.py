a=0
b=1
sum=0
print("Fabonacci Series:",end=" ")
print(0,1,end=" ")
for i in range(0,10):
    sum=a+b
    a=b
    b=sum
    print(sum,end=" ")
    