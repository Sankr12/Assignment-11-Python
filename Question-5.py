# Write a python script to calculate sum of first even natural numbers

print()
num = int(input("Enter N number: "))
b=0

for a in range(1,num+1):
    b=b+a*2

print("The sum of first N even natural numbers:",b)
print()