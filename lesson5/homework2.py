file = open('homework2.txt', 'r', encoding='UTF-8')
lines = file.readlines()
print(f'Файил содержет {len(lines)} строки')
for line in lines:
    print(f"В строке {line.count(' ') +1} слова")
file.close()
