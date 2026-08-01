file = open('15_open.py')
for line in file:
    line = line.strip()
    if line.startswith('for'):
        print(line)