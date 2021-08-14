T1 = ("am", "learning", "enjoying")
T2 = ("i", "python", "it", "alot")
a = input("enter the desired string")
b=a.split(" ")
print(b)
c=len(b)
print(c)
for b1 in b:
    for v in T1:
        if(b1==v):
            print("the element", b1, "is found in T1")
for b2 in b:
    for w in T2:
        if(b2==w):
            print("the element", b2, "is found in T2")



x = input("enter the string")
y=x.split(" ")
print(y)
z=len(y)
print(z)
T1 = ("is", "can", "be", "instructed", "carry", "programming", "have", "follow", "called", "enable", "perform", "are", "help", "learn")
T2 = ("A", "computer", "a", "machine", "that", "to", "out", "sequences", "of", "arithmetic", "or", "logical", "operations", "automatically", "via", "modern", "the",
      "ability", "generalized", "sets", "programs", "these", "an", "extremely", "wide", "range", "tasks", "very", "useful", "person", "better")
for y1 in y:
    for a in T1:
        if(y1==a):
            print("the element", y1,  "is found in T1")
for y2 in y:
    for b in T2:
        if(y2==b):
            print("the element", y2, "is found in T2")





