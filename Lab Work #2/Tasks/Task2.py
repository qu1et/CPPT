#Зададим список строк
rost = ['html', 'css', 'redis', 'http', 'https', 'vk.com/honestx', 'green paper', 'react']

#Выведем список
print("\n")
print(rost)
print("\n")

#Вывод срок длинной от 5 до 10
for i in range(0, len(rost)):
    if (len(rost[i]) >= 5 and len(rost[i]) <= 10):
        print(rost[i] + "\n")

input("Для завершения работы нажмите ENTER...")