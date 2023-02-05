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
        self.btn_sputnik.setFocusPolicy(False)
        self.btn_schema.setFocusPolicy(False)
        self.btn_hybrid.setFocusPolicy(False)

        self.btn_sputnik.clicked.connect(self.buttons_change_mode)
        self.btn_schema.clicked.connect(self.buttons_change_mode)
        self.btn_hybrid.clicked.connect(self.buttons_change_mode)
        self.Image_show()
        # self.coordinates = ''

    def initUI(self):
        uic.loadUi('map_window.ui', self)

    def Image_show(self, update=False, ll=(0, 0)):
        if not update:
            data = self.map.geocode(self.address)
            image = QImage().fromData(data)
            self.map_img.setPixmap(QPixmap(image))
            resp = self.map.get_map_info(self.address)
            self.coordinates = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point'][
                'pos'].split(' ')
        else:
            coordinates = [float(i) for i in self.coordinates]
            coordinates[0] += ll[0]
            coordinates[1] += ll[1]
            coordinates = [str(i) for i in coordinates]
            self.coordinates = coordinates
            data = self.map.get_map(coordinates[0], coordinates[1])
            image = QImage().fromData(data)
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
                self.Image_show(True)
        if event.key() == Qt.Key_Right:
            self.Image_show(True, (0.01, 0))
        if event.key() == Qt.Key_Left:
            self.Image_show(True, (-0.01, 0))
        if event.key() == Qt.Key_Up:
            self.Image_show(True, (0, 0.01))
        if event.key() == Qt.Key_Down:
            self.Image_show(True, (0, -0.01))
        # self.Image_show()

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
ex = App('Приморский край, Владивосток, площадь Борцов Революции')
ex.show()
sys.exit(app.exec())
