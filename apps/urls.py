from django.urls import path

from apps.views import home, kirish, ornatish, izoh, ozgaruvchi, malumot_turi, sonlar, satr, mantiq, operator, list_, \
    tuple_, set_, if_, funksiya, while_, massiv, sinfobject, meros, modul, data, json, try_, fayl, test, contact

urlpatterns = [
    path('', home, name='home'),
    path('Введение/', kirish, name='kirish'),
    path('Установка', ornatish, name='ornatish'),
    path('Комментарии', izoh, name='izoh'),
    path('Переменная', ozgaruvchi, name='ozgaruvchi'),
    path('Типы-данных', malumot_turi, name='malumot_turi'),
    path('Числа', sonlar, name='sonlar'),
    path('Строка', satr, name='satr'),
    path('Boolean', mantiq, name='mantiq'),
    path('Операторы', operator, name='operator'),
    path('Список', list_, name='list'),
    path('Кортеж', tuple_, name='tuple'),
    path('Множество', set_, name='set'),
    path('Условный-оператор', if_, name='if'),
    path('Функция', funksiya, name='funksiya'),
    path('Цикл', while_, name='while'),
    path('Массив', massiv, name='massiv'),
    path('Классы-и-объекты', sinfobject, name='sinfobject'),
    path('Наследование', meros, name='meros'),
    path('Модуль', modul, name='modul'),
    path('Дата', data, name='data'),
    path('json', json, name='json'),
    path('try', try_, name='try'),
    path('файла', fayl, name='fayl'),
    path('test', test, name='test'),
    path('contact/', contact, name='contact')
]
