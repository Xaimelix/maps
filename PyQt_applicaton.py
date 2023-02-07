import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow

from geocoder_request import *


class App(QMainWindow):
    def __init__(self, address: str):
        super().__init__()
        self.initUI()
        self.address = address
        self.map = Map()
        self.prime_address()
        self.Image_show()
        # self.coordinates = ''

    def initUI(self):
        uic.loadUi('map_window.ui', self)
        self.btn_sputnik.setFocusPolicy(False)
        self.btn_schema.setFocusPolicy(False)
        self.btn_hybrid.setFocusPolicy(False)

        self.btn_sputnik.clicked.connect(self.buttons_change_mode)
        self.btn_schema.clicked.connect(self.buttons_change_mode)
        self.btn_hybrid.clicked.connect(self.buttons_change_mode)

    def prime_address(self):
        data = self.map.geocode(self.address)
        self.coordinates = [float(i) for i in data]

    def Image_show(self, ll=(0, 0)):
        self.coordinates = [self.coordinates[0] + ll[0], self.coordinates[1] + ll[1]]
        data_bytes = self.map.get_map(self.coordinates[0], self.coordinates[1])
        image = QImage().fromData(data_bytes)
        self.map_img.setPixmap(QPixmap(image))


    def keyPressEvent(self, event):
        correct = True

        if event.key() == Qt.Key_PageUp or event.key() == Qt.Key_PageDown:
            if event.key() == Qt.Key_PageDown:
                k_delta = 2
                correct = self.map.change_delta(k_delta)
            if event.key() == Qt.Key_PageUp:
                k_delta = 0.5
                correct = self.map.change_delta(k_delta)
            if correct:
                self.Image_show()
        delta = float(self.map.get_delta())
        if event.key() == Qt.Key_Right:
            self.Image_show((delta, 0))
        if event.key() == Qt.Key_Left:
            self.Image_show((-delta, 0))
        if event.key() == Qt.Key_Up:
            self.Image_show((0, delta))
        if event.key() == Qt.Key_Down:
            self.Image_show((0, -delta))


    def buttons_change_mode(self):
        if self.sender() == self.btn_sputnik:
            mode = 'sat'
        elif self.sender() == self.btn_schema:
            mode = 'map'
        else:
            mode = 'sat,skl'
        correct = self.map.change_mode(mode)
        if correct:
            self.Image_show()


app = QApplication(sys.argv)
ex = App('Приморский край, Владивосток, Кипарисовая 4')
ex.show()
sys.exit(app.exec())
