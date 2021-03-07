import requests
import json
# write your code here!

cache = {}  # Словарь для хранения курсов обмена валюты для текущей сессии


def init_cache(currency_code):  # Метод для загрузки курса текущей валюты в USD и EUR в кэш
    r = requests.get('http://www.floatrates.com/daily/' + currency_code + '.json').content
    json_obj = json.loads(r)
    if currency_code != 'usd':
        cache['usd'] = json_obj['usd']['rate']
    if currency_code != 'eur':
        cache['eur'] = json_obj['eur']['rate']


exit = 0  # Переменная для контроля состояния выхода
first_currency_code = str(input()).lower()  # Читаем код валюты, которую будем обменивать
init_cache(first_currency_code)  # Загружаем курс выбранной валюты к доллару и евро

while exit == 0:  # Пока программа не в состоянии выхода
    second_currency_code = str(input()).lower()  # Читаем код валюты, на которую будем менять
    if second_currency_code != "":  # Если введена не пустая строка
        amount = float(input())  # Читаем количество денег, которое будем менять

        print('Checking the cache...')  # Сообщаем о начале проверки кэша
        if second_currency_code in cache:  # Если в кэше есть курс нужной валюты
            print('Oh! It is in the cache!')  # Сообщаем о наличии курса в кэше
        else:  # Если нужного курса валюты нет в кэше
            print('Sorry, but it is not in the cache!')  # То сообщаем об этом пользователю
            # Добавляем курс необходимой валюты в кэш
            r = requests.get('http://www.floatrates.com/daily/' + first_currency_code + '.json').content
            json_obj = json.loads(r)
            cache[second_currency_code] = json_obj[second_currency_code]['rate']

        answer = amount * cache[second_currency_code]  # Считаем, сколько мы получим денег
        print('You received {} {}.'.format(round(answer, 2), second_currency_code.upper()))

    else:  # Если введена пустая строка
        exit = 1  # Тогда переводим программу в состояние выхода
