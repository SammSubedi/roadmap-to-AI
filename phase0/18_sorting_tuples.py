d = {'a': 10, 'd':3, 'b':1, 'c':2}
print("Unsorted:",d)
t = sorted(d.items())
print("Sorted:",t)

for a,b in t:
    print (a,b)