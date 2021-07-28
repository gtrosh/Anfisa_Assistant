import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

def what_temperature(weather):    
    if (weather == '<сетевая ошибка>' or
        weather == '<ошибка на сервере погоды. попробуйте позже>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature

def what_conclusion(parsed_temperature):
    try:
        # Приведите parsed_temperature к типу int
        # и сохраните полученное число в переменную temperature
        temperature = int(parsed_temperature)

        # Теперь можно сравнивать temperature с заданными пределами 18°С и 27°С
        # и возвращать нужные фразы в зависимости от результатов сравнения.
        
        if temperature < 18: # Если (if) температура строго меньше 18:
            return 'Ой-ой-ой, слишком холодно, чтобы есть мороженое!' # вернуть (return) фразу со словом 'холодно'
        elif 18 <= temperature <= 27:
        # Если температура в диапазоне от 18 до 27 включительно
            return 'Сейчас мороженое - в самый раз!' # вернуть фразу со словами 'в самый раз'
        else: # В остальных случаях:
            return 'Ух как жарко, скорей ешь мороженое!' # вернуть фразу со словом 'жарко'
            
    except ValueError:
        return 'Не могу узнать погоду. Решай по обстоятельствам: съесть ли мороженое сразу или отложить до жары.'
        # Если parsed_temperature не удалось преобразовать в число —
        # значит, погодный сервис сломался и надо вернуть фразу "Не могу узнать погоду..."
