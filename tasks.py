# 1. Какие шаги ты бы предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?
'''
1. Сообщить администратору сайта, при возможности.
2. Пользователю подождать, когда администратор сайта решит проблему.
3. Если у меня есть доступ к сайту и я администратор, то проверяла бы результаты мониторинга и алерты и
в дальнейшем действовала в зависимости от ситуации, в то числе в зависимости от того, на чем развернут web-server
'''


# 2. Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить? Исправь ошибку и перепиши код ниже с использованием типизации.

'''
Функция callback при вызове имеет в локальном пространстве последний step = 4,
значит это значение надо передать в lambda функцию, чтобы она при своем вызове передавала нужный step в функцию callback
'''
from typing import Callable

def create_handlers(callback: Callable) -> list:
   handlers = []
   for step in range(5):
      # добавляем обработчики для каждого шага (от 0 до 4)
      handlers.append(lambda step=step: callback(step))

   return handlers

def execute_handlers(handlers: list):
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()


# 3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы выше.
'''
При попытке доступа к сайту из кода, вот такое приходит:
<html dir="ltr" lang="ru">
<head>
<meta charset="utf-8"/>
<title>Доступ запрещен</title>
</head>
<body>
<h1>Доступ к сайту greenatom.ru запрещён</h1>
<p>Для разблокировки предоставьте информацию с этой страницы в службу поддержки сайта</p>
<pre>Request ID: 2023-06-16-10-19-52-3A53C51E2B0822B3</pre>
<pre>Client IP: 000.00.00.000</pre>
<pre>Time stamp: 2023-06-16T10:19:52Z</pre>
<pre>BR</pre>
</body>
</html>


поэтому и теги считаются неправильно
'''
import requests
from lxml import html
from collections import Counter

url = 'https://greenatom.ru'
page = requests.get(url)
tree = html.fromstring(page.content)

all_elms = tree.cssselect('*')
all_tags = [x.tag for x in all_elms]
all_elms = list(filter(lambda x: len(x.attrib) > 0, all_elms))

c = Counter(all_tags)

for e in c:
    print('{}: {}'.format(e, c[e]))

print('Кол-во тагов с аттрибутами: ', len(all_elms))


# 4. Напиши функцию на Python, которая возвращает текущий публичный IP-адрес компьютера (например, с использованием сервиса ifconfig.me).
def get_ip():
    import http.client
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    print(conn.getresponse().read())

# 5. Напиши функцию на Python, выполняющую сравнение версий. Условия:
#  - Return -1 if version A is older than version B
#  - Return 0 if versions A and B are equivalent
#  - Return 1 if version A is newer than version B
#  - Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.

def check_versions(A: str, B: str):
    def split_ver(V):
        return [*map(int, V.split("."))]

    a = split_ver(A)
    b = split_ver(B)

    difflen = len(a) - len(b)
    if difflen > 0:
        b.extend([0] * difflen)
    elif difflen < 0:
        a.extend([0] * (-difflen))
    lna = len(a)-1

    for i in range(len(a)):
        if a[i] < b[i]:
            return -1
            break
        elif a[i] > b[i]:
            return 1
            break
        elif a[i] == b[i]:
            if i >= lna:
                return 0

# 6. Напиши функцию, которая возвращает True, если список содержит как минимум одну пару противоположных значений (например 5 и -5).
def check_list_1(lst):
    for i in lst:
        return True if -i in lst else None

def check_list_2(lst):
    l = (-i in lst for i in lst)
    for n in l:
        return n if n == True else None