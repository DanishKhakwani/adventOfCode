#!/usr/bin/python3.4

import re

with open('inputs/5.txt', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()


def stringCheckPart1(my_list):

    vowels = ['a', 'e', 'i', 'o', 'u']
    badStrings = ['ab', 'cd', 'pq', 'xy']
    niceStringCount = 0

    for string in my_list:
        # Vowel count
        vCount = 0
    
        niceString = False
    
        # at least 3 vowels check
        for pos, char in enumerate(string):
            if char in vowels:
                vCount += 1
                if vCount == 3:
                    niceString = True
                    break
        
        if niceString == False:
            continue

        # Repeated letters check
        p = re.compile(r'(\w)\1*')
        regexCheck = [ match.group() for match in p.finditer(string) ]

        if not(len(max(regexCheck, key=len))) >= 2:
            continue

        # Bad strings check
        for subStr in badStrings:
            if subStr in string:
                niceString = False
                break
            else:
                niceString = True

        if niceString == False:
            continue

        # Incrementing count if all checks pass
        niceStringCount += 1

    return niceStringCount

def stringCheckPart2(my_list):
    
    niceStringCount = 0

    # Pair of strings and no overlapping check
    for string in my_list:
        chars = 0
        niceString = False

        while chars+1 != len(string):
            charPair = string[chars]+string[chars+1]

            matcher = re.compile(charPair)
            regexCheck = [ match.group() for match in matcher.finditer(string) ]
            if not(len(regexCheck)) >= 2:
                chars += 1
                continue
            else:
                niceString = True
                break
        
        if niceString == False:
            continue

        niceString = False 
        chars = 0

        while chars+2 != len(string):
            charsJoin = string[chars]+string[chars+1]+string[chars+2]

            if charsJoin == charsJoin[::-1]:
                niceString = True
                break

            chars += 1

        if niceString == True:
            niceStringCount += 1

    return niceStringCount

print(stringCheckPart1(my_list))
print(stringCheckPart2(my_list))
