from random import *
print("Привіт! я загадав число від 1 до 100")
print('У тебе 7 спроб,щоб його вгадати')
a=randint(1,100)
c=0
i=0
while (c!=a or i<=6):
 b=input('Введи своє припущення')
 c=int(b)
 i=i+1
 if c<a:
     print('Замале')
 elif c>a:
     print('Завелике')
 else:
     print ('Ти вгадав, молодець! Купи собі шоколадку')
     break
if c!=a:
     print('Кількість спроб вичерпано. З тебе 100 грн')