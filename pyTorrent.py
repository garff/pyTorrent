import sys, os

from pyTorrent.controller.controller import Controller
from pyTorrent.model.model import Model
from pyTorrent.view.view import View

'''
    Created July 13, 2020
    @author: Mads Garff
    @version: 1.0.0
'''

class PyTorrent:
    def __init__(self):
        self.view = View()
        self.model = Model()
        self.controller = Controller(self.model, self.view)

if __name__ == '__main__':
    pyTorrent = PyTorrent()