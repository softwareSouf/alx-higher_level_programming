#!/usr/bin/python
if __name__ == "__main__":

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a // b}

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        result = operators[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    except ValueError:
    print("Invalid input. Please enter integers for a and b.")
