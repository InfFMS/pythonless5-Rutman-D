# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
import random
n = int(input())
a = [random.randint(1, 1000) for _ in range(n)]

print(a)

new_lst = [*reversed([a[i] for i in range(len(a) // 2)]), *reversed([a[i] for i in range(len(a) // 2, len(a))])]

print(*new_lst)