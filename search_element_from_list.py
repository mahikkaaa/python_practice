#program to count the appearance of an element in a list
a=["aa", "aa", "aa", "bb", "bb", "bb", "bb", "bb", "bb", "bb", "vv", "cc"]
print(a)
b=input("enter any element from the list")
c=0
d=len(a)
print(d)
f=0
while(c<d):
    e=a[c]
    if(e==b):
        f=f+1
    c=c+1
print("the entered element has appeared", f, "times")


#program to search an element from the string
x = ("""A computer is a machine that can be instructed to carry out sequences of arithmetic or logical
 operations automatically via computer programming. modern computer have the
  ability to follow generalized sets of operations, called programs. these programs
   enable computer to perform an extremely wide range of tasks. programs are very useful, programs help a person learn better""")
y=x.split(" ")
print(y)
z=input("enter any word from x")
a=0 #a is the index for the list y
b=len(y)
print(b)
c=0 #c is the counter to make the loop work
while(a<b):
    d=y[a]
    if(z==d):
        c=c+1
    a=a+1
print("the entered word has appeared", c, "times")


