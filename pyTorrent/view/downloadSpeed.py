import PyQt5.QtWidgets as QtWidgets

class DownloadSpeed(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        self.setText("D: 50 mb/s")
