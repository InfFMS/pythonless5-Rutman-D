# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
from random import randint
n = int(input())
a = [randint(-100, 100) for x in range(n)]
print(a)
a1=[i for i in a if i>0]
a2=[i for i in a if i<0]
a3=[i for i in a if i==0]
b=a1+a2+a3

print(b)