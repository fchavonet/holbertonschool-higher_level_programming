#!/usr/bin/python3
for number in range(00, 100):
    if number < 99:
        print("{:02}".format(number), end=", ")
    else:
        print("{}".format(number))
