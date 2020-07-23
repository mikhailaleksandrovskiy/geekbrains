# 6) Реализовать два небольших скрипта:  а) итератор, генерирующий целые
# числа, начиная с указанного,  б) итератор, повторяющий элементы списка a)
# Подсказка: использовать функцию ​count() и cycle() модуля ​itertools​.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
# повторение элементов списка будет прекращено.

import time
from itertools import count, cycle
from sys import argv

script_name, param1 = argv
print('Homework Lesson6', script_name)

numbers = count(int(param1))
numbers_iter = iter(numbers)
numbers_list = []

for num in numbers_iter:
    numbers_list.append(num)
    print(numbers_list)
    time.sleep(0.2)
    if num == int(param1) + 14:
        break

numbers_repeat = []

i = 0
for el in cycle(reversed(numbers_list)):
    if i > 14:
        break
    numbers_repeat.append(el)
    print(numbers_repeat)
    time.sleep(0.2)
    i += 1
