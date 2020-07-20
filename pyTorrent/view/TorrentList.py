import PyQt5.QtWidgets as QtWidgets


class TorrentList(QtWidgets.QListWidget):

    def __init__(self):
        super().__init__()

        # Allows for selection of several items at once holding ctrl/shift
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
