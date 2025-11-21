a = input("Введите цифру: ")
b = input("Введите цифру: ")
c = input("Введите цифру: ")
numberstr = a + b + c
number = int(numberstr)
print(number)


z = input("Введите четырехзначное число: ")
j = int(z[0]) * int(z[1]) * int(z[2]) * int(z[3])
print(j)


meters = float(input("Введите метры: "))
centimeters = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
miles = meters / 1609.34
print(meters)
print(centimeters)
print(decimeters)
print(millimeters)
print(miles)


base = float(input("Введите длину основания : "))
height = float(input("Введите высоту : "))
area = 0.5 * base * height
print(area)


p = input("Введите четырехзначное число: ")
if len(p) == 4 and p.isdigit():
    reversednumber = p[::-1]
    print(p)
    print(reversednumber)
















































