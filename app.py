from flask import Flask, render_template, redirect, url_for, request
from ya_maps import get_yandex_map, get_coordinates_by_name


app = Flask(__name__)


@app.route('/')
def index():
    """
    Возвращает главную страницу
    :return:
    """
    return render_template('form-city.html')


@app.route('/get-card', methods=['POST'])
def get_card():
    """
    Возвращает карту пользователю
    :return:
    """
    city = request.form.get('city')
    layer = request.form.get('layer')
    print(city, layer)
    coords = get_coordinates_by_name(city)
    filename = get_yandex_map(coords, layer)
    if filename == 'ERROR':
        return 'Ошибка запроса'
    return render_template('results.html', filename=filename)


if __name__ == "__main__":
    # Запуск приложения
    app.run(debug=True)
