x = ("""A computer is a machine that can be instructed to carry out sequences of arithmetic or logical
 operations automatically via computer programming. modern computers have the
  ability to follow generalized sets of operations, called programs. these programs
   enable computers to perform an extremely wide range of tasks. programs are very useful, programs help a person learn better""")
y=x.count("computer")
z=x.count("program")
m=int(y)
print(m)
n=int(z)
print(n)
if(m>n):
    print("computer is greater than program")
    p=x.replace("computer", "laptop")
    print(p)
elif(n>m):
    print("program is greater than computer")
    q=x.replace("program", "code")
    print(q)
o=x.split("computer")
print(o)

