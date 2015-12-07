#!/usr/bin/python3.4

# open file for reading
with open('2.txt', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()

print(my_list)

wrapPaper = 0

for dim in my_list:
    paper = 0
    print(dim)
    #l, w, h = dim.split('x')
    l, w, h = [int(x) for x in dim.split('x')]
    print("Length: " + str(l))
    print("Width: " + str(w))
    print("Height: " + str(h))
    
    paper = 2*(l*w + w*h + h*l)
    lst = [l*w, w*h, h*l]
    smallestSide = min(lst)
    print("Smallest Side = " + str(smallestSide))
    paper += int(smallestSide)

    print("Paper = " + str(paper))
    wrapPaper += paper

print("Wrap Paper: " + str(wrapPaper))


#### PART 2 ####

totalRibbon = 0
for dim in my_list:
    ribbon = 0

    l, w, h = [int(x) for x in dim.split('x')]
    print("Length: " + str(l))
    print("Width: " + str(w))
    print("Height: " + str(h))
    
    lst = [l, w, h]
    firstMin = min(lst)
    lst.remove(firstMin)
    secondMin = min(lst)
    lst.remove(secondMin)
    print("Short list: " + str(lst))
    
    ribbon = 2*(firstMin + secondMin)
    bow = l*w*h
    totalRibbon += ribbon + bow

print("totalRibbon = " + str(totalRibbon))

