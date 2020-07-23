# 5) Реализовать формирование списка, используя функцию ​range() и возможности генератора. В
# список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка. Подсказка: использовать функцию ​reduce()​.

import random
from functools import reduce

list = [0] * 4
for el in range(len(list)):
    list[el] = random.randint(100, 1000)

print(list)

def result(a, b):
    return a + b

print(reduce(result, list))

