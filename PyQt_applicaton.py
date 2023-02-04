import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.initUI()
        self.img = image_path

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Map')

    def Image_show(self):
        pic = QLabel(self)
        pic.setPixmap(QPixmap(self.img))
        pic.show()  # You were missing this.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())