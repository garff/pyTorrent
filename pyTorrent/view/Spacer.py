import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import *

class Spacer(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        self.setText(" - ")
        self.setAlignment(Qt.AlignCenter)
