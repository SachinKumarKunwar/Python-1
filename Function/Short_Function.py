def add(num1,num2):
    print(num1+num2)
x=int(input("Enter a number:"))
y=int(input("Enter second number:"))
add(x,y)


#  or
#lambda function
x=lambda num1,num2 : num1+num2
print(x(3,4))


# Short Function

cars=["bmw","tesla","nano","swift desire"]
[print(x) for x in cars]


newlist=[x for x in cars if x!="Tata"]
print(newlist)
