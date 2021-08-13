program to reverse a number
a=int(input("enter any 3 digit number to be reversed"))
b=int(a/10)
c=int(b/10)
print(c)
d=b%10
print(d)
e=a%10
print(e)
f=0
f=f*10+e
f=f*10+d
f=f*10+c
print("the reversed number is",f)