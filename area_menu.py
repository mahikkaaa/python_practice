#to find the area of a shape of your desired choice
shape=int(input("to find the area of circle press 1, to find the area of triangle press 2, to find the area of rectangle press 3 - "))
if(shape==1):
    r=float(input("enter the radius of the circle to be calculated"))
    pi=3.14
    area_of_circle = pi*r*r
    print("the area of circle is", area_of_circle)
if(shape==2):
    b=float(input("enter the base of the triangle to be calculated"))
    h = float(input("enter the height of the triangle to be calculated"))
    area_of_triangle = 0.5*b*h
    print("the area of triangle is", area_of_triangle)
if(shape==3):
    b=float(input("enter the base of the rectangle to be calculated"))
    l = float(input("enter the length of the rectangle to be calculated"))
    area_of_rectangle = b*l
    print("the area of rectangle is", area_of_rectangle)