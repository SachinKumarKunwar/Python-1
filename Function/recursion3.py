#Fabonacci Series
def fabonacci(num):
    sum=0
    return num+fabonacci(num)
ans=fabonacci(10)
print(ans)