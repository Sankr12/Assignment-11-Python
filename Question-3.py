# Write a python script to calculate sum of cubes of first N natural numbers

print()
N = int(input("Enter N number: ")) 

b=0
for a in range(1,N+1):
    b=b+a**3

print("The sum of cubes of N natural numbers:",b)
print()