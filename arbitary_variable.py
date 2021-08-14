#use of arbitary variable
def about(**m):
    print("name is",m["a"])
    print("age is", m["b"])
    print("gender is", m["c"])
about(a="mahika", b="18", c="F")

f1=input("enter first name")
f2=input("enter last name")
def name(**m):
    print("first name is",m["a"])
    print("last name is",m["b"])
    print("the complete name is", m["a"]+ " "+ m["b"])
name(a=f1, b=f2)

def area1(**m):
    choice=input("press 1 to find the area of circle and press 2 to find the area of rectangle")
    if(choice=="1"):
        circle=3.14*r*r
        print("the area of circle is", circle)
    elif(choice=="2"):
        rectangle=l*b
        print("the area of rectangle is", rectangle)
r=float(input("enter the radius"))
l=float(input("enter the length"))
b=float(input("enter the breadth"))
area1()


