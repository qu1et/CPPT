#Задаем список со строками и числами
roster = [1, 'a', 'v', 12, 'sr', 20, 'det', 'f', 'g', 1, 4]

#Выводим четные элементы построчно
for i in range(0, len(roster)):
    if i % 2 == 0:
        print(roster[i])

input('Press ENTER to exit')