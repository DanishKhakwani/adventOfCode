#!/usr/bin/python3.4

with open('3.txt', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()



def generateCoordList(my_list):
    
    coordinates=[0,0]
    lst=["0:0"]

    for char in my_list[0]:
        if char == '^':
            coordinates[0]+=1
        elif char == 'v':
            coordinates[0]-=1
        elif char == '>':
            coordinates[1]+=1
        else:
            coordinates[1]-=1
    
        lst.append(str(coordinates[0])+":"+str(coordinates[1]))
    
    return lst

lst=generateCoordList(my_list)
totalHouses=len(lst)

print("Total houses = " + str(totalHouses))

# Unique Houses

#for coord, pos in enumerate(lst):
#    print(coord)
#    print(pos)

unique_lst = [
        e
        for i, e in enumerate(lst)
        if lst.index(e) == i
]

print("Houses = " + str(len(unique_lst)))

# Part II
santaList=[""]
roboList=[""]
for pos, char in enumerate(my_list[0]):
    #print("Character = " + char)
    #print("Position = " + str(pos))

    if pos % 2 == 0:
        santaList[0]+=char
    else:
        roboList[0]+=char

#print(santaList)
#print(roboList)
finalList=["0:0"]
finalList=generateCoordList(santaList)
finalList+= generateCoordList(roboList)
#print(finalList)

unique_lst = [
        e
        for i, e in enumerate(finalList)
        if finalList.index(e) == i
]
print("Total houses = " + str(len(finalList)))
print("Houses = " + str(len(unique_lst)))
