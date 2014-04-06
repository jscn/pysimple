# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Machine(object):

    def __init__(self, expression, environment):
        self._expression = expression
        self._environment = environment

    def step(self):
        self._expression = self._expression.reduce(self._environment)

    def run(self):
        while self._expression.is_reducible:
            print self._expression
            self.step()
        print self._expression


class Variable(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{0}'.format(self.name)

    def __repr__(self):
        return self.__str__()

    @property
    def is_reducible(self):
        return True

    def reduce(self, environment):
        return environment[self.name]
