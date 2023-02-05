import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PIL import *
from geocoder_request import *


class App(QMainWindow):
    def __init__(self, address: str):
        super().__init__()
        self.initUI()
        self.address = address
        self.map = Map()
        self.Image_show()

    def initUI(self):
        uic.loadUi('map_window.ui', self)

    def Image_show(self):
        data = self.map.get_map(self.address)
        image = QImage().fromData(data)
        self.map_img.setPixmap(QPixmap(image))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp or event.key() == Qt.Key_PageDown:
            c_d = 0.01
            if event.key() == Qt.Key_PageUp:
                print(1)
                self.map.change_delta(-c_d)
            if event.key() == Qt.Key_PageDown:
                self.map.change_delta(c_d)
            self.Image_show()




app = QApplication(sys.argv)
ex = App('Приморский край, Владивосток, площадь Борцов Революции')
ex.show()
sys.exit(app.exec())