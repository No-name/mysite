# -*- coding: utf-8 -*-

class NoEscape(object):
    def __init__(self, content):
        self._inner = content

    def __xml__(self):
        return self._inner

    def __len__(self):
        return len(self._inner)