# Write a python script to calculate sum of first N odd natural numbers 

print()
num = int(input("Enter N numbers: "))
p=0

for a in range(1,num+1):
    p=p+(a*2)-1

print("The sum of first N odd natural numbers:",p)
print()