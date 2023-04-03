#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        if self.width not int:
            print("TypeError width must be an integer")
        if self.width < 0:
            print("ValueError width must be >=0")
        return self.width

    def height(self):
        if self.height not int:
            print("TypeError height must be an integer")
        if self.height < 0:
            print("ValueError height must be >=0")
        return self.heightdef __init__(self, width=0, height=0):
