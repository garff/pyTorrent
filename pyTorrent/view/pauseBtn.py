import PyQt5.QtWidgets as QtWidgets

class PauseBtn(QtWidgets.QPushButton):

    def __init__(self):
        super().__init__()

        self.setText("Pause")
