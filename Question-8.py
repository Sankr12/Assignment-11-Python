# Write a python script to calculate sum of digits of a given number

print()
num = int(input("Enter a number: "))
a = 0

while num>0:
    b=num%10
    a=a+b
    num=num//10

print("The sum of digits of a given number:",a)
print()
