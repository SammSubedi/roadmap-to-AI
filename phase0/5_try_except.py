name = input("Enter your name: ")
try:
    int(name)
    print('Not a name')
except ValueError:
    print("Hello", name)
