# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
from random import randint
N = int(input())
result = [randint(0,100) for i in range(N)]
while True:
    s = input()
    if not s:
        break
    if s not in result:
        result.append(s)
print(result)
