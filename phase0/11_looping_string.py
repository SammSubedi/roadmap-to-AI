name = input("Enter name: ")
count = 0
for char in name:
    print (char, count )
    count = count + 1

count = 0
print("new line")
for i in range(len(name)):
    char = name[i]
    print(char, count)
    count = count + 1