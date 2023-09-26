#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]

    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        number1 = int(argv[1])
        number2 = int(argv[3])

        if operator == '+':
            result = add(number1, number2)
        elif operator == '-':
            result = sub(number1, number2)
        elif operator == '*':
            result = mul(number1, number2)
        elif operator == '/':
            if number2 == 0:
                print("Division by zero is not allowed.")
                exit(1)
            result = div(number1, number2)

        print("{} {} {} = {}".format(number1, operator, number2, result))
