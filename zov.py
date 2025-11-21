a = int(input("Введите начало диапазона: "))
d = int(input("Введите конец диапазона: "))
print(a, d)
for number in range(a, d + 1):
    if number % 7 == 0:
        print(number)


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

print("\n1. Все числа диапазона:")
for number in range(start, end + 1):
    print(number, end=" ")

print("\n\n2. Все числа диапазона в убывающем порядке:")
for number in range(end, start - 1, -1):
    print(number, end=" ")

print("\n\n3. Все числа, кратные 7:")
count_7 = 0
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number, end=" ")
        count_7 += 1
if count_7 == 0:
    print("нет таких чисел")

print("\n\n4. Количество чисел, кратных 5:")
count_5 = 0
for number in range(start, end + 1):
    if number % 5 == 0:
        count_5 += 1
print(f"Найдено чисел: {count_5}")


h = int(input("Введите начало диапазона: "))
j = int(input("Введите конец диапазона: "))

print(f"\nFizzBuzz для диапазона от {h} до {j}:")

for number in range(h, j + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)





































































