import requests

def geocode(human_address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": human_address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    return response