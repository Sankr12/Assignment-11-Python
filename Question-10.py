# Write a python script to print octal equivalent of a given decimal number

print()
num=int(input("Enter a number: "))
i=num

b=''
while num>0:
    a=num%8
    b=str(a)+b
    num=num//8

print("Octal Equivalent of",i,'=',b)
print()
