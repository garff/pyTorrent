from ..model.model import Model
from ..view.view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.register(self)
        self.view.initUI()

    def addTorrent(self, filename: str):
        """
        Adds a torrent to the database. 

        :return void 
        """
        newTorrentList = self.model.addTorrent(filename)
        self._updateTorrentListView(newTorrentList)

    def _updateTorrentListView(self, newTorrentList: list):
        """
        Updates the view regarding the currently added torrents.
        
        :return void 
        """
        print(self.__dict__)
        self.view.torrentList.updateTorrentList(newTorrentList)