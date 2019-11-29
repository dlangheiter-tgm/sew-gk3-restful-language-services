from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import MyView
import sys
import requests

class MyController(QMainWindow):

    def click_check(self):
        text = self.myForm.input.toPlainText()

        try:
            resp = requests.get("http://localhost:8080", params={"text": text})
        except Exception as e:
            print(e)
            return

        json = resp.json()
        print(json)
        out = "reliable: <b>" + str(json["reliable"]) + "</b><br>"
        out += "language: <b>" + json["language"] + "</b><br>"
        out += "probability <b>" + str(json["prob"]) + "</b><br>"
        self.myForm.output.clear()
        self.myForm.output.append(out)

    def __init__(self):
        """
        Constructor
        """
        super().__init__(None)

        self.myForm = MyView.Ui_MainWindow()
        self.myForm.setupUi(self)

        self.myForm.check.clicked.connect(self.click_check)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
