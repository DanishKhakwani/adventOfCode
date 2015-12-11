#!/usr/bin/python3.4

import re

with open('test.txt', 'r') as infile:
    data = infile.read()

hexa = re.compile(r'\\x..')
quote = re.compile(r'^(\\")$')
backslash = re.compile(r'\\\\')
my_list = data.splitlines()

literal_count = 0
charInMem_count = 0

for string in my_list:
    literal_count += len(string)

    print(string)
    hexChars = len([match.group() for match in hexa.finditer(string)])
    quotes = len([match.group() for match in quote.finditer(string)])
    backslashChars = len([match.group() for match in backslash.finditer(string)])
    print("Hex = " + str(hexChars))
    print("Quotes = " + str(quotes))
    print("Backslash = " + str(backslashChars))
    print([match.group() for match in hexa.finditer(string)])
    print([match.group() for match in quote.finditer(string)])
    print([match.group() for match in backslash.finditer(string)])

    charInMem_count += len(string)-2-(hexChars*3+quotes+backslashChars)
    
print("-------------RESULT---------------")
print(literal_count)
print(charInMem_count)
print(literal_count-charInMem_count)
