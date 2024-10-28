# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.

from random import randint
arr = []
N = int(input())
a = [0]*N
for i in range(N):
  print ( "A[", i, "] =", sep = "", end = "" )
  a[i] = int(input())



n = len(a)
arrm = a[0]
c = 1
for i in range(1, n):
    if a[i] >= arrm:
        if a[i] > arrm:
            arrm = a[i]
            c = 1
        else:
            c += 1
print(c)

