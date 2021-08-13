#WHILE LOOP
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


#FOR LOOP
#program to make sub list from list without using split function
a=["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh"]
b=len(a)
print(b)
d=[]
e=[]
for c in range(b):
    f=c%2
    #print(f)
    if(f==0):
        d.append(a[c])
    elif(f!=0):
        e.append(a[c])
    c=c+1
print(d)
print(e)


#program to make string to sub list from list without using split function
x = ("""A computer is a machine that can be instructed to carry out sequences of arithmetic or logical
 operations automatically via computer programming. modern computer have the
  ability to follow generalized sets of operations, called programs. these programs
   enable computer to perform an extremely wide range of tasks. programs are very useful, programs help a person learn better""")
y=x.split(" ")
print(y)
z=len(y)
print(z)
a=[]
b=[]
for c in range(z):
    d=c%2
    if(d==0):
        a.append(y[c])
    elif(d!=0):
        b.append(y[c])
print(a)
print(b)

