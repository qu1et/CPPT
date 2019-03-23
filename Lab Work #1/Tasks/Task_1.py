#Ввод данных
a = float(input("Введите значение переменной а:  "))
b = float(input("Введите значение переменной b:  "))
c = float(input("Введите значение переменной с:  "))
k = float(input("Введите значение переменной k:  "))

#Обработка исключений
try:
    res = abs((a**2 / b**2 + c**2 * a**2) / (a + b + c * (k - a / b**3)) + c + (k / b - k / a) * c)
except ZeroDivisionError:
    print("Деление на нуль невозможно!\nВведите значения а и b снова")
    a = float(input("Введите значение переменной а:  "))
    b = float(input("Введите значение переменной b:  "))
    res = abs((a**2 / b**2 + c**2 * a**2) / (a + b + c * (k - a / b**3)) + c + (k / b - k / a) * c)

#Вывод
print("Ответ:  " + str(res))

input('Press ENTER to exit')