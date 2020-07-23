# 2. Представлен список чисел. Необходимо вывести элементы
# исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

random_numbers = []
random_numbers_len = random.randint(10,20)
i = 0
while i != random_numbers_len:
    random_numbers.append(random.randint(0,1000))
    i+=1

print(random_numbers)

result = []
i = 1

while i != random_numbers_len:
    if random_numbers[i] > random_numbers[i-1]:
        result.append(random_numbers[i])
        i += 1
    else:
        i += 1
print(result)


