# Write a pthon script to print binary equivalent of a given decimal number

print()
num = int(input("Enter a number: "))
b=""
i=num

while num>0:
    a=num%2
    b=str(a)+b
    num=num//2

print("Binary equivalent of",i,"=",b)
print()