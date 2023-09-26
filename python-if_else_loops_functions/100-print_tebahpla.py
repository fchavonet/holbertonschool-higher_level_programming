#!/usr/bin/python3

for i in range(122, 96, -1):
    
    if i % 2 == 0:
        char_to_print = chr(i)
    else:
        char_to_print = chr(i - 32)

    print(char_to_print, end='')
