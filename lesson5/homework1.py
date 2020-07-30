strings = 1000000
content_list = []

for string in range(strings):
    content_list.append(input('Введите строку: '))
    if content_list[string] == '':
        break

content = " \n".join(content_list)

file = open('homework.txt', 'w', encoding='UTF-8')
file.write(content)
file.close()
