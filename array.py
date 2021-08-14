import array as ar
a=ar.array('i', [1, 2, 3, 4, 5])
x = 10
b = 0
while (b < x):
    y = int(input("enter any value"))
    a.append(y)
    b = b + 1
print(a)
pop=a.pop(6)
print(a)



a = []
from array import *
T = [[1,2,3,10], [4,5,6,11], [7,8,9,12], [13,14,15,16]]
print(T[1],T[0],T[2])
x=0
y=0
while (x<4):
    while(y==x):
        print(T[x][y])
        m=T[x][y]
        y = y + 1
        a.append(m)
    x = x + 1
    D = sum(a)
    print(D)
print(a)
def sum():
    d=0
    e=0
    b = len(a)
    print(b)
    for c in range (0,b):
        d=a[c]
        print(d)
        e=e+d
    print(e)
sum()

