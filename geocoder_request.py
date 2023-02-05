import requests


class Map():
    def __init__(self):
        self.map_type = 'map'

    def geocode(self, human_address):
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": human_address,
            "format": "json"}

        response = requests.get(geocoder_api_server, params=geocoder_params)
        # print(response)
        # print(response.content)
        return response

    def get_map(self):
        api_server = "http://static-maps.yandex.ru/1.x/"

        lon = "37.530887"
        lat = "55.703118"
        delta = "0.002"

        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([delta, delta]),
            "l": self.map_type
        }
        response = requests.get(api_server, params=params)
        return response.content