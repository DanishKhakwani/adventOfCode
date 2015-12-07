#!/usr/bin/python3.4

# open the file for reading.
with open('1.txt', 'r') as infile:

        data = infile.read()  # Read the contents of the file into memory.

# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()

print(my_list)

floor=0
position=1
for char in my_list[0]:
    print(char)
    if char == '(':
        floor+=1
    else:
        floor-=1
    if floor < 0:
        break
    position+=1
print(floor)
print(position)
