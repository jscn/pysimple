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
