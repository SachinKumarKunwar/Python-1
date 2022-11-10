# Factorial 
def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)

num=int(input("Enter a number:"))
print("Factorial of given number is:")
print(factorial(num))