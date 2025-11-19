#задание 1

x = int(input("text"))
if x < 1 or x > 100:
    print("Ошибка ввода данных")
if x%3==0 or x%5==0:
    print("Fizz Buzz")
elif x%3==0:
    print("Fizz")
elif x%5==0:
    print("Buzz")
else:
    print(x)

#задание 2

x = int(input("введи число которое возводим в указанную степень "))
s = int(input("укажите степень от 1 до  7"))
if s < 1 or s > 7:
    print("степень не вернная")
else:
    print(x ** s)

# задание 3


duration = float(input("Введите длительность разговора (мин): "))
from_operator = input("С какого оператора (МТС/Билайн/МегаФон/Теле2): ")
to_operator = input("На какой оператор (МТС/Билайн/МегаФон/Теле2): ")

if from_operator == "МТС":
    if to_operator == "МТС":
        cost = duration * 1
    elif to_operator == "Билайн":
        cost = duration * 2
    elif to_operator == "МегаФон":
        cost = duration * 2
    elif to_operator == "Теле2":
        cost = duration * 3
    else:
        cost = 0

elif from_operator == "Билайн":
    if to_operator == "МТС":
        cost = duration * 2
    elif to_operator == "Билайн":
        cost = duration * 1
    elif to_operator == "МегаФон":
        cost = duration * 2
    elif to_operator == "Теле2":
        cost = duration * 3
    else:
        cost = 0

elif from_operator == "МегаФон":
    if to_operator == "МТС":
        cost = duration * 2
    elif to_operator == "Билайн":
        cost = duration * 2
    elif to_operator == "МегаФон":
        cost = duration * 1
    elif to_operator == "Теле2":
        cost = duration * 2
    else:
        cost = 0

elif from_operator == "Теле2":
    if to_operator == "МТС":
        cost = duration * 3
    elif to_operator == "Билайн":
        cost = duration * 3
    elif to_operator == "МегаФон":
        cost = duration * 2
    elif to_operator == "Теле2":
        cost = duration * 1
    else:
        cost = 0

else:
    cost = 0

if cost > 0:
    print(f"Стоимость разговора: {cost} руб.")
else:
    print("Ошибка в выборе оператора")


# задача 4

#module 2 task 4
prise = 200
manager_1 = int(input())
manager_2 = int(input())
manager_3 = int(input())

if manager_1 < 500:
    manager_1 = prise+manager_1/100*3
elif manager_1 >= 500 and manager_1 < 1000:
    manager_1 = prise+manager_1/100*5
else:
    manager_1 = prise+manager_1/100*8

if manager_2 < 500:
    manager_2 = prise+manager_2/100*3
elif manager_2 >= 500 and manager_2 < 1000:
    manager_2 = prise+manager_2/100*5
else:
    manager_2 = prise+manager_2/100*8

if manager_3 < 500:
    manager_3 = prise+manager_3/100*3
elif manager_3 >= 500 and manager_3 < 1000:
    manager_3 = prise+manager_3/100*5
else:
    manager_3 = prise+manager_3/100*8

if manager_1 > manager_2 and manager_1 > manager_3:
    print('manager_1 лучший работник с зарплатой = ', manager_1+200, '\nmanager_2 = ',manager_2, '\nmanager_3 = ',manager_3)
elif manager_2 > manager_1 and manager_2 > manager_3:
    print('manager_2 лучший работник с зарплатой = ', manager_2+200, '\nmanager_1 = ',manager_1, '\nmanager_3 = ',manager_3)
else:
    print('manager_3 лучший работник с зарплатой = ', manager_3+200, '\nmanager_1 = ',manager_1, '\nmanager_2 = ',manager_2)










































