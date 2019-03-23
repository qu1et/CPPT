#Задаем список чисел
rost = [10, 41, 99, 80, 55, 71, 65, 100, 7, 71]

#Иництализируем переменную для максимума
max = rost[0]

#Поиск наибольшего числа в списке
for i in range(1, len(rost)):
    if max < rost[i]:
        max = rost[i]

#Выводим ответ
print("Максимальное число в списке:  " + str(max))

input('Press ENTER to exit')