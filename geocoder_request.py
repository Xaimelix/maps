import requests


class Map():
    def __init__(self):
        self.map_type = 'map'
        self.delta = '0.002'

    def geocode(self, human_address) -> list:
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": human_address,
            "format": "json"}

        response = requests.get(geocoder_api_server, params=geocoder_params).json()

        toponym = response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"].split(' ')

        return toponym_coodrinates

    def get_map(self, lon, lat) -> bytes:
        api_server = "http://static-maps.yandex.ru/1.x/"
        self.lon = str(lon)
        self.lat = str(lat)
        params = {
            "ll": ",".join([self.lon, self.lat]),
            "spn": ",".join([self.delta, self.delta]),
            "l": self.map_type
        }
        response = requests.get(api_server, params=params)
        return response.content

    def get_map_info(self, address):
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": address,
            "format": "json"}

        response = requests.get(geocoder_api_server, params=geocoder_params).json()
        return response

    def change_delta(self, k_delta):
        if 0.00015 < float(self.delta) * k_delta < 10:
            self.delta = str(float(self.delta) * k_delta)
            return True
        else:
            return False

    def get_delta(self):
        return self.delta

    def change_mode(self, mode):
        if self.map_type != mode:
            self.map_type = mode
            return True
        else:
            return False
