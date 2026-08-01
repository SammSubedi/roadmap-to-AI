num = [1,65,22,32,55,88]

# a = num[0]
a = None

for largest in num:

    # use is for boleans or None
    if a is None:
        a =  largest
    elif a < largest:
        a = largest
    # if a < largest:
    #     a = largest
print(a)