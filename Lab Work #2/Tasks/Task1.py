#Подключим библиотеку random
import random

#Зададим рандомное число
my_number = random.randint(0, 20)

#Запрашиваем и cчитываем число
user_nummber = int(input("Введите число от 0 до 20:  "))

#Запрашиваем число у пользователя, пока оно не совпадет с рандомным
while (user_nummber != my_number):
    user_nummber = int(input("Введите число от 0 до 20:  "))

#Выводим обращение
print("Вы угадали!\nИсходное число: " + str(user_nummber))

input("Для завершения работы нажмите ENTER...")