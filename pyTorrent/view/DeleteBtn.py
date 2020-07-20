import PyQt5.QtWidgets as QtWidgets


class DeleteBtn(QtWidgets.QPushButton):

    def __init__(self):
        super().__init__()

        self.setText("Delete")
