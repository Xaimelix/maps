import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from geocoder_request import geocode, get_map


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.img = image_path
        self.Image_show()
    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Map')

        self.map = QLabel(self)
        self.map.setGeometry(0, 0, 400, 400)

    def Image_show(self):

        data = get_map()
        image = QImage()
        image.loadFromData(data)
        self.map.setPixmap(QPixmap(image))
        # pic.show()  # You were missing this.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())