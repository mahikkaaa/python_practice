#using for loop
a=["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj"]
c=input("enter any alphabet set")
for b in a:
    if(b == c):
        print("found")
        break
    elif(b != c):
        print("not found")


#printing range using for loop
y=int(input("enter the range"))
for x in range(y):
    print(x)

#TO FIND prime numbers using for loop
a=int(input("enter the number "))
f=0
for c in range(2,a+1):
    d=a%c
    if(d==0):
        f=f+1
    c=c+1
if(f==1):
    print("the number is prime")
if(f!=1):
    print("the number is not prime")


#to find if the number is even or odd
a=int(input("enter the number "))
for c in (2,3):
    d=a%c
    if(d==0):
        print("the number is even")
    elif(d!=0):
        print("the number is odd")
