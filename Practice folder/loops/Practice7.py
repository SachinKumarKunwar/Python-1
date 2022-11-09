n=int(input("Enter a number:"))
sum=0
for a in range(1,n+1):
    if n%a==0:
        sum+=a
print(sum)