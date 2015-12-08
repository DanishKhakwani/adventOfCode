#!/usr/bin/python3.4

with open('7.txt', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()

dic = {}

operands = ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']

for command in my_list:
    command = command.split('->')
    print(command)

