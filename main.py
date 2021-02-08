import sys


from PyQt5.Qt import QMainWindow, QApplication
from PyQt5 import uic


class AppMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("data/map-ui.ui", self)

        self.pushButton.clicked.connect(self.show_map)

        self.server = "http://static-maps.yandex.ru/1.x/"

    def show_map(self):
        try:
            coords = [float(self.lineEdit.text()), float(self.lineEdit_2.text())]
        except:
            self.statusBar().showMessage("Неверный формат координат", 1000)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AppMainWindow()
    main_window.show()
    app.exec()
