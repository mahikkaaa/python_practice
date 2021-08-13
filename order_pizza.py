program to order pizza
print("welcome to united pizza outlet")
"1"=="veg pizza"
"2"=="non veg pizza"
print("for veg pizza choose 1 and for non-veg pizza choose 2")
choice=int(input("inter your preference"))
if(choice==1):
    print("""for veg pizza, the options are-
             paneer
             cheese""")
    veg=input("enter your veg pizza prefernce")
    if(veg=="paneer"):
        print("the price is inr 150")
        paneer=150
        quantity=int(input("enter the number of pizza required"))
        price=paneer*quantity
        print("the total amount is",price)
    if (veg == "cheese"):
        print("the price is inr 200")
        cheese = 200
        quantity = int(input("enter the number of pizza required"))
        price = cheese * quantity
        print("the total amount is", price)
if(choice==2):
    print("""for non-veg pizza, the options are-
             chicken
             prawn""")
    nonveg = input("enter your veg pizza prefernce")
    if (nonveg == "chicken"):
        print("the price is inr 350")
        chicken = 350
        quantity = int(input("enter the number of pizza required"))
        price = chicken * quantity
        print("the total amount is", price)
    if (nonveg == "prawn"):
        print("the price is inr 400")
        prawn = 400
        quantity = int(input("enter the number of pizza required"))
        price = prawn * quantity
        print("the total amount is", price)


