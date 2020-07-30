file = open('homework4.txt', 'r', encoding='UTF-8')
data = file.readlines()

numbers = ['Один', 'Два', 'Три', 'Четыре']
new_file = {}
i = 0
for line in data:
    content = line.split(' ')
    content[0] = numbers[i]
    i+=1
    new_file[i] = content
    print(content)

file.close()

file = open('homework4B.txt', 'w', encoding='UTF-8')
for num, content in new_file.items():
    file.write(" ".join(content))

file.close()
