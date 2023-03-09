#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    elif sys.argv[2] == '+':
        func = add
    elif sys.argv[2] == '-':
        func = sub
    elif sys.argv[2] == '*':
        func = mul
    elif sys.argv[2] == '/':
        func = div
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    result = func(int(sys.argv[1]), int(sys.argv[3]))
    print("{:d} {:s} {:d} = {:d}".format(int(sys.argv[1]),
        sys.argv[2], int(sys.argv[3]), result))