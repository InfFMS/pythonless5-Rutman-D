# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N = 3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import math
import random

random.seed()

N = int(input())

a = [random.randint(0,1000) for i in range(N)]
b = [random.randint(0,1000) for i in range(N)]

sum = 0
s1 = 0
s2 = 0

for i in range(len(a)):
    sum += a[i]*b[i]
    s1 += (a[i])**2
    s2 += (b[i])**2


print(math.degrees(math.acos(sum/((s1**0.5)*(s2**0.5)))))
