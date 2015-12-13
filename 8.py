#!/usr/bin/python3.4

with open('inputs/8.txt', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()

literal_count = 0
charInMem_count = 0
encoded = 0

for string in my_list:
    literal_count += len(string)

    charInMem_count += len(eval(string))
    encoded += len(string)-string.count('"')-string.count('\\')+ \
            2+string.count('\\')*2+string.count('"')*2
            
# Part I
print(literal_count-charInMem_count)
# Part II
print(encoded-literal_count)
