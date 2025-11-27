# Вправа 1 — Форматуй дату через strftime
# Напиши програму, яка:
# отримує поточну дату й час (datetime.now())
# виводить у трьох форматах:
#
# "DD-MM-YYYY"
# "YYYY/MM/DD HH:MM"
# "Today is: Saturday"
#
# Приклад результату:
#
# 22-11-2025
# 2025/11/22 17:45
# Today is: Saturday

from datetime import datetime
now=datetime.now()
# print(now(strftime("%d-%m-%Y")))
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%Y/%m/%d %H:%M"))
print(now.strftime("Today is: %A"))

# Вправа 2 — Різниця між двома датами
#
# Створи дві дати:
#
# 2025-01-01
#
# 2024-05-10
#
# Обчисли:
#
# різницю в днях
#
# різницю в тижнях
#
# різницю в годинах
#
# Очікувано:
#
# Днів: ...
# Тижнів: ...
# Годин: ...

from datetime import datetime

date1 = datetime(2025, 1, 1)
date2 = datetime(2024, 5, 10)

delta = date1 - date2   # різниця між датами

print("Днів:", delta.days)
print("Тижнів:", delta.days // 7)
print("Годин:", delta.days * 24)

# Вправа 3 — Час до Нового року
#
# Напиши програму, яка:
# бере поточний момент (datetime.now())
# створює дату наступного Нового року
# виводить:
# скільки днів залишилось
# скільки годин
# скільки хвилин
#
# Приклад:
#
# До Нового року: 39 днів, 8 годин, 11 хвилин

from datetime import datetime
now = datetime.now()

from datetime import datetime

now = datetime.now()
next_new_year = datetime(now.year + 1, 1, 1)

delta = next_new_year - now

days = delta.days
hours = delta.seconds // 3600       # секунди → години
minutes = (delta.seconds % 3600) // 60

print(f"До Нового року: {days} днів, {hours} годин, {minutes} хвилин")
