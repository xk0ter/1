num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
print("\nВыберите операцию:")
print("1 - Сумма трех чисел")
print("2 - Произведение трех чисел")
choice = input("Ваш выбор (1 или 2): ")
if choice == "1":
    result = num1 + num2 + num3
    print(f"Сумма чисел: {num1} + {num2} + {num3} = {result}")
elif choice == "2":
    result = num1 * num2 * num3
    print(F"Произведение чисел: {num1} × {num2} × {num3} = {result}")
else:
    print("Неверный выбор операции")


z = float(input("Введите первое число: "))
x = float(input("Введите второе число: "))
a = float(input("Введите третье число: "))
print("\nВыберите операцию:")
print("1 - Максимум из трех чисел")
print("2 - Минимум из трех чисел")
print("3 - Среднеарифметическое трех чисел")
choice = input("Ваш выбор (1, 2 или 3): ")
if choice == "1":
    maximum = max(z, x, a)
    print(f"Максимум из чисел {z}, {x}, {a}: {maximum}")
elif choice == "2":
    minimum = min(z, x, a)
    print(f"Минимум из чисел {z}, {x}, {a}: {minimum}")
elif choice == "3":
    average = (z + x + a) / 3
    print(f"Среднеарифметическое чисел {z}, {x}, {a}: {average:.2f}")
else:
    print("Неверный выбор операции")


meters = float(input("Введите количество метров: "))
print("\nВыберите единицу измерения для перевода:")
print("1 - Мили")
print("2 - Дюймы")
print("3 - Ярды")
j = input("Ваш выбор (1, 2 или 3): ")
if j == "1":
    miles = meters * 0.000621371
    print(f"{meters} метров = {miles:.6f} миль")
elif j == "2":
    inches = meters * 39.3701
    print(f"{meters} метров = {inches:.2f} дюймов")
elif j == "3":
    yards = meters * 1.09361
    print(f"{meters} метров = {yards:.2f} ярдов")
else:
    print("Неверный выбор")






































