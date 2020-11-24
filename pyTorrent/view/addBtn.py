import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class AddBtn(QtWidgets.QPushButton):

    def __init__(self, controller):
        super().__init__()
        self.setText("Add")
        self.controller = controller
        self.clicked.connect(self.onInputAddBtnClicked)

    def onInputAddBtnClicked(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"Torrent file", "","Torrent files (*.torrent)")        

        if fileName:
            self.controller.addTorrent(fileName)