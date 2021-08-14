class AB:
    c = 0
    def sum1(self,a,b):
        c=a+b
        print(c)
    def sum1(self):
        d=6
        e=5
        f=d+e
        print(f)
A = AB()
print("the sum is", A.c)
a = int(input("enter any number"))
b = int(input("enter any number"))
A.sum1()
A.sum1()

#
class HELLO:
    def swap(self,a,b):
        a,b=b,a
        print("the new value of a is", a)
        print("the new value of b is", b)
M = HELLO()
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
print("the original a is",a)
print("the original b is",b)
M.swap(a,b)