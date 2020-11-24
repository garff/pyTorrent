from PyQt5 import QtWidgets as QtW

class TorrentList(QtW.QListWidget):

    def __init__(self):
        super().__init__()

        # Allows for selection of several items at once holding ctrl/shift
        # self.setSelectionMode(QtWidgets.Q)

    def updateTorrentList(self, torrentList):
        self.clear() # clears the current torrents from the list 

        for torrent in torrentList:
            item = QtW.QListWidgetItem("Test item " + str(torrent)) 
            self.addItem(item)