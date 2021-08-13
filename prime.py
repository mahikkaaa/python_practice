#program to check if the number is prime or not
a=int(input("enter any number "))
c=2
f=0
while(c<=a):
    d=a%c
    if(d==0):
        f=f+1
    c=c+1
if(f==1):
    print("the number is prime")
elif(f!=1):
    print("the number is not prime")