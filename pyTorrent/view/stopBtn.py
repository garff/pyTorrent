import PyQt5.QtWidgets as QtWidgets


class StopBtn(QtWidgets.QPushButton):

    def __init__(self):
        super().__init__()

        self.setText("Stop")
