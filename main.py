import sys
from io import BytesIO
import requests
from geocoder_request import geocode
from PIL import Image
from PyQt_applicaton import *

address = 'Москва, ул. Ак. Королева, 12'

response = geocode(address)

if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([delta, delta]),
    "l": "map",
    "size": '450,450'
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).save('res.png')

app = QApplication(sys.argv)
ex = Example('res.png')
ex.show()
sys.exit(app.exec())
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы