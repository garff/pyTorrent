import PyQt5.QtWidgets as PyQt5

from pyTorrent.pyTorrent.view.StartBtn import StartBtn
from pyTorrent.pyTorrent.view.PauseBtn import PauseBtn
from pyTorrent.pyTorrent.view.StopBtn import StopBtn
from pyTorrent.pyTorrent.view.DeleteBtn import DeleteBtn
from pyTorrent.pyTorrent.view.TorrentList import TorrentList
from pyTorrent.pyTorrent.view.DownloadSpeed import DownloadSpeed
from pyTorrent.pyTorrent.view.Spacer import Spacer
from pyTorrent.pyTorrent.view.UploadSpeed import UploadSpeed

class View():

    def __init__(self, controller):
        super(View, self).__init__()
        self.controller = controller

        app = PyQt5.QApplication([])

        ## Setting up main window
        mainWindow = PyQt5.QWidget()
        mainWindow.resize(600,600)
        mainWindow.setWindowTitle("pyTorrent v.1.0")

        ## Adding UI widgets 
        self.layout = PyQt5.QGridLayout()

        # Buttons 
        self.layout.addWidget(StartBtn(), 0, 0)
        self.layout.addWidget(PauseBtn(), 0, 1)
        self.layout.addWidget(StopBtn(), 0, 2)
        self.layout.addWidget(DeleteBtn(), 0, 10)

        # Item list holding the torrents
        self.torrentList = TorrentList() 
        self.layout.addWidget(self.torrentList, 1, 0, 1, 11)

        # Adding test torrents 
        for x in range(10):
            item = PyQt5.QListWidgetItem("Test item " + str(x))
            self.torrentList.addItem(item)

        # Adding download / uploads speeds 
        self.layout.addWidget(DownloadSpeed(), 2, 8)
        self.layout.addWidget(Spacer(), 2, 9)
        self.layout.addWidget(UploadSpeed(), 2, 10)

        mainWindow.setLayout(self.layout)
        mainWindow.show()

        app.exec_()
