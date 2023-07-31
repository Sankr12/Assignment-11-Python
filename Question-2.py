# Write a python script to calculate the sum of squares of first N natural numbers

print()
N = int(input("Enter N numbers: "))
b=0

for i in range(1,N+1):
    b=b+i**2

print("The sum of squares of N natural numbers:",b)
print()