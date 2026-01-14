def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap(2020))
print(leap(2025))
print(leap(2000))
print(leap(1900))