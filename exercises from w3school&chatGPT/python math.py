# Вправа 1 — Квадратний корінь і степені
#
# Використовуючи модуль math:
# Запроси у користувача число.
# Виведи:
# квадрат цього числа
# квадратний корінь
# число в степені 3
#
# Приклад:
#
# Введи число: 9
# Квадрат: 81
# Корінь: 3.0
# Куб: 729

import math
a = int(input("Enter a number: "))
c = a * a
print(f"The square of {a} is {c}")
b = math.sqrt(a)
print(f"The square root of {a} is {b}")
# d = a * c
d = math.pow(a, 3)
print(f"The cube of {a} is {d}")

# Вправа 2 — Площа кола
#
# Використай math.pi.
# Запроси у користувача радіус.
# Обчисли площу кола.
# Округли до 2 знаків (math.ceil або math.floor, або round).
#
# Приклад:
#
# Введи радіус: 5
# Площа кола: 78.54

import math
r = float(input("Enter a radius: "))
s = math.pi * r**2
s = round(s, 2)
print(f"The area of round with radius {a} is {s}")

# Вправа 3 — Факторіал числа
#
# Використай math.factorial().
#
# Запроси у користувача число n
# Виведи факторіал
#
# Приклад:
#
# Введи число: 6
# Факторіал: 720

import math
num = int(input("Enter a number: "))
fac = math.factorial(num)
print(f"The factorial of {num} is {fac}")