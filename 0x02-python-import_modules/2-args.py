#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()
print(len(sys.argv[1:]), "arguments:")
index = 1
while index <= len(sys.argv[1:]):
   print("{}: {}".format(index, sys.argv[index]))
   index += 1
