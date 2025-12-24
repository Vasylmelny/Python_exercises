# Напиши програму, яка запитує два числа і виводить результат ділення.
# Оброби помилки:
#
# ділення на нуль
#
# введення нечислових значень

try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    result = a / b
    print("Результат:", result)

except ZeroDivisionError:
    print("Помилка: ділення на нуль!")

except ValueError:
    print("Помилка: введено не число!")

# Напиши програму, яка намагається відкрити файл data.txt.
# Оброби помилки:
#
# файл не знайдено
#
# ненадійні операції читання

filename = "data.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        print("Вміст файлу:")
        print(content)

except FileNotFoundError:
    print("Помилка: файл не знайдено!")

except IOError:
    print("Помилка: проблема з читанням файлу!")

# Є список значень. Спробуй конвертувати всі елементи в числа.
# Якщо якийсь елемент не конвертується — вивести повідомлення і пропустити його.

values = ["10", "5.5", "hello", "3", "world"]

numbers = []

for v in values:
    try:
        num = float(v)
        numbers.append(num)
    except ValueError:
        print(f"Неможливо конвертувати: {v}")

print("Список чисел:", numbers)