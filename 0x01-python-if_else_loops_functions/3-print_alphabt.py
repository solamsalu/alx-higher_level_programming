#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z')+1):
    letter = chr(alpha_letters)
    if letter not in "qe":
        print(letter, end="")
