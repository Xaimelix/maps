import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic
from PIL import *
from geocoder_request import *


class Example(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.initUI()
        self.img = image_path
        self.Image_show(image_path)

    def initUI(self):
        uic.loadUi('map_window.ui', self)

    def Image_show(self, image_path):
        self.pixmap = QPixmap(image_path)
        self.map.setPixmap(self.pixmap)
        # data = Map().get_map()
        # image = QImage()
        # image.loadFromData(data)
        # print(image)
        # self.map.setPixmap(QPixmap(image))
        # pic.show()  # You were missing this.