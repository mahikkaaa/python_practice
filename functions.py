def python():
    print("i am in function")
python()


#program to find areas
def circle():
        r = float(input("enter the radius of circle"))
        area_of_circle = 3.14 * r * r
        print("the area of circle is", area_of_circle)
def triangle():
        b=float(input("enter the base of the triangle"))
        h =float(input("enter the height of the triangle"))
        area_of_triangle = 0.5*b*h
        print("the area of triangle is", area_of_triangle)
def rectangle():
        l=float(input("enter the length of the rectangle"))
        w=float(input("enter the width of the rectangle"))
        area_of_rectangle = l*b
        print("the area of rectangle is", area_of_rectangle)
area=input("for circle press 1, for triangle press 2, for rectangle press 3")
if(area=="1"):
    circle()
if(area=="2"):
    triangle()
if(area=="3"):
    rectangle()


#program to order pizza
def pizza():
    option_P=input("for veg pizza press 1, for non veg press 2")
    if(option_P=="1"):
        veg=input("for cheese press 1, for chocolate press 2")
        if(veg=="1"):
            cheese = 350
            print("the price is 350 inr")
            quantity_cheese = int(input("enter the quantity"))
            amount_1=cheese*quantity_cheese
            print(amount_1)
        if (veg=="2"):
            chocolate = 500
            print("the price is 500 inr")
            quantity_chocolate = int(input("enter the quantity"))
            amount_2=chocolate*quantity_chocolate
            print(amount_2)
        total_P_amount = amount_1 + amount_2
    if (option_P == "2"):
        nonveg = input("for chicken press 1, for prawn press 2")
        if (nonveg == "1"):
            chicken = 550
            print("the price is 550 inr")
            quantity_chicken = int(input("enter the quantity"))
            amount_1 = chicken * quantity_chicken
            print(amount_1)
        if (nonveg == "2"):
            prawn = 800
            print("the price is 800 inr")
            quantity_prawn = int(input("enter the quantity"))
            amount_2 = prawn * quantity_prawn
            print(amount_2)
        total_P_amount = amount_1 + amount_2
def beverage():
    option_B=input("for coffee press 1, for soft drinks press 2")
    if (option_B == "1"):
        coffee = input("for hot coffee  press 1, for cold coffee press 2")
        if (coffee == "1"):
            hot_coffee = 150
            print("the price is 150 inr")
            quantity_HC = int(input("enter the quantity"))
            amount_1 = hot_coffee * quantity_HC
            print(amount_1)
        if (coffee == "2"):
            cold_coffee = 200
            print("the price is 200 inr")
            quantity_CC = int(input("enter the quantity"))
            amount_2 = cold_coffee * quantity_CC
            print(amount_2)
    if (option_B == "2"):
        soft_drink = input("for pepsi  press 1, for fanta press 2")
        if (soft_drink == "1"):
            pepsi = 15
            print("the price is 15 inr")
            quantity_pepsi = int(input("enter the quantity"))
            amount_1 = pepsi * quantity_pepsi
            print(amount_1)
        if (soft_drink == "2"):
            fanta = 20
            print("the price is 20 inr")
            quantity_fanta = int(input("enter the quantity"))
            amount_2 = fanta * quantity_fanta
            print(amount_2)

print("welcome to united pizza")
choice=input("for pizza press 1, for beverage press 2")
if(choice=="1"):
    pizza()
if(choice=="2"):
    beverage()

#program to call a
def swap():
    x = int(input("enter any number:"))
    y = int(input("enter any number:"))
    print("the orginal x is",x)
    print("the original y is",y)
    x,y=y,x
    print("the new x is",x)
    print("the new y is",y)
swap()

def swap():
    x = int(input("enter any number:"))
    y = int(input("enter any number:"))
    print("the orginal x is",x)
    print("the original y is",y)
    a=x
    x=y
    y=a
    print("the new x is", x)
    print("the new y is",y)
swap()
