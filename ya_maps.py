from requests import get
from random import randint

API_SEARCH_MAPS = 'b13d9f55-8288-4733-b69b-ed23208db109'
API_STATIC_MAPS = '3ee39648-05d4-4c6e-a2fd-29bc72ecc96f'


def get_coordinates_by_name(name: str) -> list:
    url = 'https://search-maps.yandex.ru/v1/'
    query_params = {
        'apikey': API_SEARCH_MAPS,
        'text': name,
        'lang': 'ru_RU',
        'type': 'geo'
    }
    response = get(url, params=query_params)
    response = response.json()
    print(response)
    return response['features'][0]['geometry']['coordinates']


def get_yandex_map(coordinates: list, layer: str = 'map') -> str:
    url = 'https://static-maps.yandex.ru/1.x/'
    coordinates = list(map(str, coordinates))
    params = {
        'll': ','.join(coordinates),
        'spn': ','.join(('0.05', '0.05',)),
        'l': layer,
        'apikey': API_STATIC_MAPS,
    }
    resp = get(url, params=params)
    if resp.status_code == 200:
        filename = f'map_{randint(1, 100000)}.png'
        try:
            with open('static/img/' + filename, 'wb') as f:
                f.write(resp.content)
            return filename
        except IOError:
            print('Ошибка! Файл не удалось сохранить!')
            return 'ERROR'
    else:
        print(f'Ошибка №{resp.status_code}')
        print(resp.text)
        return 'ERROR'
