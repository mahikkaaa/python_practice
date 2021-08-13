#program to swap numbers (using three variables)
a=3
print("the value of a is ",a, "and")
b=2
print("the value of b is ",b)
print("after reversal the values are")
c=a
a=b
print("the value of a after reversal is",a)
b=c
print("the value of b after reversal is",b)

#program to swap numbers (using two variables)
a=3
print("the value of a is",a)
b=2
print("the value of b is",b)
print("after reversal the values are")
a=a+b
print("the new value of a is",a)
b=a-b
a=a-b
print("the value of a after reversal is",a)
print("the value of b after reversal is",b)

#swapping two numbers
a=3
b=2
print("original a",a)
print("original b",b)
a,b=b,a
print("reversed a",a)
print("reversed b",b)


