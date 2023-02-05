import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic
from PIL import *
from geocoder_request import *


class App(QMainWindow):
    def __init__(self, address: str):
        super().__init__()
        self.initUI()
        self.address = address
        self.Image_show()
        self.map = QLabel(self)


    def initUI(self):
        uic.loadUi('map_window.ui', self)

    def Image_show(self):
        data = Map().get_map(self.address)
        image = QImage().fromData(data)
        self.map.setPixmap(QPixmap(image))


app = QApplication(sys.argv)
ex = App('Приморский край, Владивосток, площадь Борцов Революции')
ex.show()
sys.exit(app.exec())