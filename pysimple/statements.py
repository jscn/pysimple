# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from copy import deepcopy


class Assign(object):

    def __init__(self, name, expression):
        self._name = name
        self._expression = expression

    def __str__(self):
        return '{0} = {1}'.format(self._name, self._expression)

    def __repr__(self):
        return self.__str__()

    @property
    def is_reducible(self):
        return True

    def reduce(self, environment):
        if self._expression.is_reducible:
            return (Assign(self._name, self._expression.reduce(environment)),
                    environment)
        else:
            # Ensure we return a new copy of the environment, rather
            # than altering the current one in place.
            new_environment = deepcopy(environment)
            new_environment.update({self._name: self._expression})
            return (DoNothing(), new_environment)


class DoNothing(object):

    def __str__(self):
        return 'do-nothing'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return type(other) == self.__class__

    @property
    def is_reducible(self):
        return False
