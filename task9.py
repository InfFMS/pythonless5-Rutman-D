# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
from random import randint
N = int(input())
r = [randint(0,5) for i in range(N)]
print(r)
a = [r[0]]
s = 0
for i in range(1, len(r)):
    s = 0
    for j in range(len(a)):
        if a[j] != r[i]:
            s+=1
        if s == len(a):
            a.append(r[i])

print(a)

