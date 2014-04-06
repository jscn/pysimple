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

    def reduce(self, environment):
        if self.left.is_reducible:
            return self.__class__(self.left.reduce(environment), self.right)
        elif self.right.is_reducible:
            return self.__class__(self.left, self.right.reduce(environment))
        return self._reduce()


class Add(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Add, self).__init__(*args, **kwargs)
        self.sign = '+'

    def _reduce(self):
        return Number(self.left.value + self.right.value)


class And(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(And, self).__init__(*args, **kwargs)
        self.sign = 'and'

    def _reduce(self):
        return Boolean(bool(self.left.value and self.right.value))


class Divide(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Divide, self).__init__(*args, **kwargs)
        self.sign = '/'

    def _reduce(self):
        return Number(self.left.value / self.right.value)


class Equal(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Equal, self).__init__(*args, **kwargs)
        self.sign = '=='

    def _reduce(self):
        return Boolean(self.left.value == self.right.value)


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


class Not(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'not {0}'.format(self.value)

    @property
    def is_reducible(self):
        return True

    def reduce(self):
        if self.value.is_reducible:
            return Not(self.value.reduce(environment))

        return Boolean(not self.value.value)


class Or(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Or, self).__init__(*args, **kwargs)
        self.sign = 'or'

    def _reduce(self):
        return Boolean(bool(self.left.value or self.right.value))


class Subtract(BinaryOperator):

    def __init__(self, *args, **kwargs):
        super(Subtract, self).__init__(*args, **kwargs)
        self.sign = '-'

    def _reduce(self):
        return Number(self.left.value - self.right.value)
