#!/usr/bin/env python3
""" Laboratory Work 1 """

class Action:
    """ This class operates with arguments"""
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def sum(self):
        """ Return sum of arguments"""
        return self.arg1 + self.arg2

    def mult(self):
        """ Return multiplication of arguments"""
        return self.arg1 * self.arg2

a = int(input('Input the first number: '))
b = int(input('Input the second number: '))

actions = Action(a, b)
print('Sum:', actions.sum())
print('Multiplication:', actions.mult())
