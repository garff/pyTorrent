# Temp Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from pyTorrent.pyTorrent.model.model import Model
from pyTorrent.pyTorrent.view.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    # def main(self):
        # self.view.main()

if __name__ == '__main__':
    controller = Controller()
    # controller.main()
    
