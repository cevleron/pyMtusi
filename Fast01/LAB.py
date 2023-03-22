# Сгенерировать последовательность 100 случайных чисел с нормальным законом распределения
# (mx=1, dx=1). Упорядочить полученную последовательность, расположив элементы по возрастанию.
# Образовать новую последовательность, состоящую из разности соседних элементов Хi-Xi-1.
# Для полученной последовательности вычислить среднее значение,
# дисперсию и вывести ее на печать в виде гистограммы, разбив диапазон на 10 интервалов.

import random
import numpy
mass = []
mass2 = []
# Создание массива с 100 случайными числами с нормальным законом распределения.
mx=1
dx=1
count = 0
while count<100:
    n = random.normalvariate(mx,dx)
    mass.append(round(n,2))
    count+=1
    #print( n, end=' ')
print(mass)
# Сортировка чисел.
print()
mass.sort()
print(mass)

for i in range(100):
    if i == 0:
       mass2.append(mass[i])
    else:
        mass2.append(round(mass[i] - mass[i-1],2))

print(mass2)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot()
ax.hist(mass2)
ax.grid()
plt.show()

