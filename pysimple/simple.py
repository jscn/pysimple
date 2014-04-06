# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Machine(object):

    def __init__(self, statement, environment):
        self._statement, self._environment = statement, environment

    def step(self):
        self._statement, self._environment  = self._statement.reduce(
            self._environment)

    def run(self):
        while self._statement.is_reducible:
            print self._statement, self._environment
            self.step()
        print self._statement, self._environment


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
