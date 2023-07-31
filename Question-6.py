# Write a python script to calculate factorial of a given number

print()
num = int(input("Enter a number: "))
b=1

for a in range(1,num+1):
    b=b*a

print("The factorial of",num,"=",b)
print()