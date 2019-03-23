#Подключение библиотеки random и string
import random
import string

y = 5
#Генерируем случайную строку
def random_char(y):
    return ''.join(random.choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") for x in range(y))

print(random_char(5))

input("Для завершения нажмите ENTER...")