#!/usr/bin/python3.4

import re

with open('6.txt', 'r') as infile:
    data = infile.read()

my_list = data.splitlines()

pattern = re.compile('\d+,\d+')

def init(op):
    dic = {}
    coord_x = 999
    coord_y = 999
    for x in range(0, coord_x+1):
        x_part = str(x)
        for y in range(0, coord_y+1):
            y_part = str(y)
            dic[x_part,y_part] = op
    return dic

def get_coords(string):
    
    lst = [ match.group() for match in pattern.finditer(string) ]
    return lst

def switch_lights(coords, dic, op):

    count = 0
    start_x, start_y = [ str(coord) for coord in coords[0].split(',') ]
    end_x, end_y = [ str(coord) for coord in coords[1].split(',') ]

    st_x = start_x

    while int(st_x) <= int(end_x):

        st_y = start_y
        
        while int(st_y) <= int(end_y):
            if dic[st_x,st_y] == 'on' and (op == 'off' or op == 'toggle'):
                dic[st_x,st_y] = 'off'
            elif dic[st_x,st_y] == 'off' and (op == 'on' or op == 'toggle'):
                dic[st_x,st_y] = 'on'

            st_y = str(int(st_y)+1)

        st_x = str(int(st_x)+1)
    return dic

def get_lights(dic):

    lights_on = 0

    coord_x = 999
    coord_y = 999
    
    for x in range(0, coord_x+1):
        x_part = str(x)
        for y in range(0, coord_y+1):
            y_part = str(y)
            if dic[x_part,y_part] == 'on':
                lights_on += 1

    return lights_on

def increase_brightness(coords, dic, op):
    
    start_x, start_y = [ str(coord) for coord in coords[0].split(',') ]
    end_x,   end_y   = [ str(coord) for coord in coords[1].split(',') ]

    st_x = start_x

    while int(st_x) <= int(end_x):

        st_y = start_y
        
        while int(st_y) <= int(end_y):
            if op == 'on':
                dic[st_x,st_y] += 1
            elif op == 'off' and dic[st_x,st_y] > 0:
                dic[st_x,st_y] -= 1
            elif op == 'toggle':
                dic[st_x,st_y] += 2

            st_y = str(int(st_y)+1)

        st_x = str(int(st_x)+1)
    return dic

def get_brightness(dic):
    
    brightness = 0

    coord_x = 999
    coord_y = 999

    for x in range(0, coord_x+1):
        x_part = str(x)
        for y in range(0, coord_y+1):
            y_part = str(y)
            brightness += dic[x_part,y_part]

    return brightness

dic = init("off")
dic2 = init(0)
for step in my_list:

    coords = get_coords(step)

    if 'turn on' in step:
        dic  = switch_lights(coords, dic, 'on')
        dic2 = increase_brightness(coords, dic2, 'on')
    elif 'turn off' in step:
        dic  = switch_lights(coords, dic, 'off')
        dic2 = increase_brightness(coords, dic2, 'off')
    else:
        dic  = switch_lights(coords, dic, 'toggle')
        dic2 = increase_brightness(coords, dic2, 'toggle')

print('Total lights lit: ' + str(get_lights(dic)))
print('Total brightness: ' + str(get_brightness(dic2)))
