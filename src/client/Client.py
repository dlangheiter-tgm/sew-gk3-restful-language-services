from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import MyView
import sys


class MyController(QMainWindow):

    def __init__(self):
        """
        Constructor
        """
        super().__init__(None)

        self.myForm = MyView.Ui_MainWindow()
        self.myForm.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
