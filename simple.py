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


class Boolean(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{0}'.format(self.value)

    @property
    def is_reducible(self):
        return False


class LessThan(object):

    def __init__(self, left, right):
        self.left, self.right = left, right

    def __str__(self):
        return '{0} < {1}'.format(self.left, self.right)

    @property
    def is_reducible(self):
        return True

    def reduce(self):
        if self.left.is_reducible:
            return LessThan(self.left.reduce(), self.right)
        elif self.right.is_reducible:
            return LessThan(self.left, self.right.reduce())
        return Boolean(self.left.value < self.right.value)


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


class Machine(object):

    def __init__(self, expression):
        self._expression = expression

    def step(self):
        self._expression = self._expression.reduce()

    def run(self):
        while self._expression.is_reducible:
            print self._expression
            self.step()
        print self._expression
