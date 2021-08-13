#conditional statement
#program to check if the entered number is even or not
x = int(input("enter any number"))
s=x/2
print(s)
if (x%2==0):
    print("the entered number is even")
if(x%2!=0):
    print("the entered number is not even")


#program to check the passcode
a=["apple", "banana"]
x = input("enter the name of any fruit")
if (x==a[0]):
    print("access given")
if (x==a[1]):
    print("access given")
if (x!=a[1] and x!=[0]):
    print("access denied")


#program to compare strings irrespective of their case(upper, lower)
a=["apple"]
b=a[0].capitalize()
c=input("enter the name of any fruit")
d=c.capitalize()
if (b==d):
    print("you got it right")
if (b!=d):
    print("better luck next time")


dictionary = {"a":"apple", "b":"banana", "c":"camel"}
d = input("enter any alphabet of your choice from a to c")
print(dictionary[d])

#number to character
a=int(input("enter any ascii value"))
m=chr(a)
print(m)
#character to number 
k=input("enter any alphabet irrespective of upper case or lower case")
d=ord(k)
print(d)

