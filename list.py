a=["apple", "banana", "cherry", "strawberry", "dog", "cat"]
print(a)
print(a[-1])
print(len(a))
print(a[1:5])
print(a[-4:-1])
c=a[1:4]
print(c) #this output will act as a new sub list for the next input
d=c[1].capitalize()
print(d)
a[1]= "blueberry"
print(a)
a[1:3] = "lion", "tiger"
print(a)