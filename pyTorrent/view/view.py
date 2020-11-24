import PyQt5.QtWidgets as PyQt5

from .startBtn import StartBtn
from .pauseBtn import PauseBtn
from .stopBtn import StopBtn
from .deleteBtn import DeleteBtn
from .torrentList import TorrentList
from .downloadSpeed import DownloadSpeed
from .spacer import Spacer
from .uploadSpeed import UploadSpeed
from .addBtn import AddBtn 

class View():

    def __init__(self):
        self.controller = None

    def initUI(self):
        app = PyQt5.QApplication([])

        ## Setting up main window
        mainWindow = PyQt5.QWidget()
        mainWindow.resize(600,600)
        mainWindow.setWindowTitle("pyTorrent v.1.0")

        ## Adding UI widgets 
        self.layout = PyQt5.QGridLayout()

        # Item list holding the torrents
        self.torrentList = TorrentList() 
        self.layout.addWidget(self.torrentList, 1, 0, 1, 11)

        # Buttons
        self.deleteBtn = DeleteBtn()

        self.layout.addWidget(StartBtn(), 0, 0)
        self.layout.addWidget(PauseBtn(), 0, 1)
        self.layout.addWidget(StopBtn(), 0, 2)
        self.layout.addWidget(AddBtn(self.controller), 0, 3)
        self.layout.addWidget(self.deleteBtn, 0, 10)

        self.deleteBtn.clicked.connect(
            lambda: self.deleteBtn.deleteTorrents(self.torrentList))

        # Adding download / uploads speeds 
        self.layout.addWidget(DownloadSpeed(), 2, 8)
        self.layout.addWidget(Spacer(), 2, 9)
        self.layout.addWidget(UploadSpeed(), 2, 10)

        mainWindow.setLayout(self.layout)
        mainWindow.show()

        app.exec_()

    def register(self, controller):
        self.controller = controller