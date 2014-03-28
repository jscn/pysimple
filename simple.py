# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Number(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{0}'.format(self.value)

    @property
    def is_reducible(self):
        return False

class Add(object):

    def __init__(self, left, right):
        self.left, self.right = left, right

    def __str__(self):
        return '{0} + {1}'.format(self.left, self.right)

    @property
    def is_reducible(self):
        return True

    def reduce(self):
        if self.left.is_reducible:
            return Add(self.left.reduce(), self.right)
        elif self.right.is_reducible:
            return Add(self.left, self.right.reduce())

        return Number(self.left.value + self.right.value)


class Multiply(object):

    def __init__(self, left, right):
        self.left, self.right = left, right

    def __str__(self):
        return '{0} * {1}'.format(self.left, self.right)

    @property
    def is_reducible(self):
        return True

    def reduce(self):
        if self.left.is_reducible:
            return Multiply(self.left.reduce(), self.right)
        elif self.right.is_reducible:
            return Multiply(self.left, self.right.reduce())

        return Number(self.left.value * self.right.value)
