#!/usr/bin/python3.4

# Input
string="1113122113"

# Solution 1
for loop in range(40):

    lst = []
    temp = ""

    for pos, char in enumerate(string):

        if pos != 0:    
            prevChar = string[pos-1]
        else:
            temp += string[pos]
            continue

        if prevChar == string[pos]:
             temp += string[pos]
        else:
            lst.append(temp)
            temp = ""
            temp += string[pos]

        if pos == len(string)-1:
            lst.append(temp)

    string = ""

    for element in lst:
        string += str(len(element)) + element[0]

print(len(string))

# Solution 2 : 10 secs faster
import re
re_d = re.compile(r'((\d)\2*)')

def replace(match_obj):
    s = match_obj.group(1)
    return str(len(s)) + s[0]

for i in range(50):
    string = re_d.sub(replace,string)
print(len(string))

# Solution 3: 3 secs faster than Solution 2
from itertools import groupby

def look_and_say(string):
    return ''.join(str(len(list(v))) + k for k, v in groupby(string))

p1 = string 
for _ in range(40):
    p1 = look_and_say(p1)
print(len(p1))

p2 = string
for _ in range(50):
    p2 = look_and_say(p2)
print(len(p2))
