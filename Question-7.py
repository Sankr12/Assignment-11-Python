# Write a python script to count digits in a given number

print()
num = int(input("Enter a number: "))
a=0

while num>0:
    num = num//10
    a=a+1

print(a)
print()