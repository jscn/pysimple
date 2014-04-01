# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .primitives import Boolean, Number


class BinaryOperator(object):

    def __init__(self, left, right):
        self.left, self.right = left, right

    def __str__(self):
        return '{left} {sign} {right}'.format(left=self.left, sign=self.sign,
                                              right=self.right)

    @property
    def is_reducible(self):
        return True

    def reduce(self):
        if self.left.is_reducible:
            return self.__class__(self.left.reduce(), self.right)
        elif self.right.is_reducible:
            return self.__class__(self.left, self.right.reduce())
        return self._reduce()


class Add(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Add, self).__init__(*args, **kwargs)
        self.sign = '+'

    def _reduce(self):
        return Number(self.left.value + self.right.value)


class Divide(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Divide, self).__init__(*args, **kwargs)
        self.sign = '/'

    def _reduce(self):
        return Number(self.left.value / self.right.value)


class GreaterThan(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(GreaterThan, self).__init__(*args, **kwargs)
        self.sign = '>'

    def _reduce(self):
        return Boolean(self.left.value > self.right.value)


class LessThan(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(LessThan, self).__init__(*args, **kwargs)
        self.sign = '<'

    def _reduce(self):
        return Boolean(self.left.value < self.right.value)


class Multiply(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Multiply, self).__init__(*args, **kwargs)
        self.sign = '*'

    def _reduce(self):
        return Number(self.left.value * self.right.value)


class Subtract(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Subtract, self).__init__(*args, **kwargs)
        self.sign = '-'

    def _reduce(self):
        return Number(self.left.value - self.right.value)
