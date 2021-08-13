#program to print 10 numbers
a=0
while(a<=10):
    print(a)
    a=a+1
print("final value",a)

#program to print the table of 2
a=0
while(a<=100):
    print("the table of 2 for multiple",a, "is", a*2)
    a=a+1


#program to print all the even numbers from 1 to 50
a=1
while(a<=500):
    b=a%2
    if(b==0):
      print("the even numbers are",a)
    a=a+1

#program to add all the numbers from 0 to 50
a=0
b=0
while(a<=5000):
    b=b+a
    a=a+1
print(b)

#program to print the elements of a list using while loop
a=0
z = ["bunty", "babli", "ramesh", "suresh", "chintu", "mintu", "mukesh", "teja", "onus", "manoj", "shekhar", "prerna", "dharmendra"]
b=len(z)
print(b)
while(a<b):
    print(z[a])
    d=z[a]
    e=d.capitalize()
    print(e)
    a=a+1






