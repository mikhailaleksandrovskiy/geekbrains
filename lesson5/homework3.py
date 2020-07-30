file = open('homework3.txt', 'r', encoding='UTF-8')
data = file.readlines()

name_revenue_dict = {}

for line in data:
    each = line.split(" ")
    name_revenue_dict[each[0]] = int(each[2])

revenue_list = []

for name, revenue in name_revenue_dict.items():
    revenue_list.append(revenue)
    if revenue < 20000:
        print(f'{name} имеет оклад менее 20 тысяч')

average = sum(revenue_list) / 4
print(f'Средняя величина дохода сотрудников состовляет {average}')

file.close()
