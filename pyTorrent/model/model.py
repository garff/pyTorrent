from ..utils.Bdecode import Bdecode
from ..utils.Bencode import Bencode
from .torrent import Torrent

from collections import OrderedDict

class Model:
    """
    The model of the whole application. 
    
    Every part of the model will come as a seperate method used to
    delegate the responsibility for each part of it.
    """
    def __init__(self):
        # super().__init__()
        self.torrents = []

        ## temp solution - hold current torrent files 


    def addTorrent(self, filename):
        """
        Decodes a torrent file given a filename and creates a new 
        torrent object. Saves this new object in the list of 
        current torrents.

        ### LATER WRITE TO THE DB AS WELL.
        :return list of all current torrents
        """ 
        decoder = Bdecode(filename)
        metaData = decoder._decode()
        torrent = Torrent(metaData)    
        self.torrents.append(torrent)
        
        return self.torrents
