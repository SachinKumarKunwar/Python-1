#Accept a number from the user 
# Calculate and print the sum of all the numbers in
# from 1 to input number 
#using for loop

num=int(input("Enter a number:"))
sum=0
for a in range(1,num+1):
    sum+=a 
print("Sum of Numbers is:",sum)
    