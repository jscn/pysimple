# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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
