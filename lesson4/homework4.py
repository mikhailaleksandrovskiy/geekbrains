# 4) Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
# порядке их следования в исходном списке. Для выполнения задания обязательно
# использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

import random

list_len = 10
numbers = [0] * list_len
for el in range(list_len):
    numbers[el] = random.randint(0,10)
print(numbers)

result = []
for i in numbers:
    if numbers.count(i) == 1:
        result.append(i)
print(result)
