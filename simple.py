# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Number(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{0}'.format(self.value)


class Add(object):

    def __init__(self, left, right):
        self.left, self.right = left, right

    def __str__(self):
        return '{0} + {1}'.format(self.left, self.right)


class Multiply(object):

    def __init__(self, left, right):
        self.left, self.right = left, right

    def __str__(self):
        return '{0} * {1}'.format(self.left, self.right)
