#program to split a 3 digit number
a=int(input("enter any 3 digit number"))
b=a%10
print(b)
d=a/10
e=int(d)
f=e%10
print(f)
g=a/100
h=int(g)
print(h)

#program to find the greatest number out of a three digit number
a=int(input("enter any 3 digit number"))
b=int(a/10)
c=int(b/10)
print(c)
d=int(b%10)
print(d)
e=a%10
f=e%10
print(f)
if(c>d and c>f):
    print("the greatest digit is",c)
if(d>c and d>f):
    print("the greatest digit is", d)
if(f>c and f>d):
    print("the greatest digit is", f)

