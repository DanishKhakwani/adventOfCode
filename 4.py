#!/usr/bin/python3.4

import hashlib

def gimmeNumber(inputStr, hashStartVal):
    number = 0
    while (True):
        m = hashlib.md5()
        string = ""
        string = inputStr+str(number) 
        m.update(string.encode("utf-8"))
        hashed = m.hexdigest()
        if hashed.startswith(hashStartVal):
            #print(number)
            #print(m.hexdigest())
            return number
        number+=1

# Part I
print(gimmeNumber("ckczppom", '00000'))
# Part II
print(gimmeNumber("ckczppom", '000000'))
