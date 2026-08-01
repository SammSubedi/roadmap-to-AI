d = {'a': 10, 'd':3, 'b':1, 'c':2}

# sorts in coparision with the second key like 1 2 3 10  coz 
# first we set (b,a) to represent the value and key and then we looped with key and value
print ( sorted ([ (b,a) for a,b in d.items() ]))