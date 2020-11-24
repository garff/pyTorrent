import PyQt5.QtWidgets as QtWidgets

class UploadSpeed(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        self.setText("U: 25 mb/s")
