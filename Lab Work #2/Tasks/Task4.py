import string
from itertools import groupby

#Считываем строку
my_str = input("Введите любую строку:  ")

#Проходим по строке и находим числа
l = [int(''.join(i)) for is_digit, i in groupby(my_str, str.isdigit) if is_digit]

st = ""
#Переносим числа в строку
for i in l:
    st += str(i)

#Выводим числа
print(st)

#Завершение
input("Для завершения нажмите ENTER...")