import os
import zipfile

answer = []

with zipfile.ZipFile('main.zip', 'r') as zipka:
    zipka.extractall()

for current_dir, dirs, files in os.walk('main'):
    for name in files:
        if name.endswith(".py"):
            if current_dir not in answer:
                answer.append(current_dir)
            break

with open('task_3.txt', 'w', encoding='UTF-8') as task3:
    task3.write('\n'.join(sorted(answer)))

with open('task_3.txt', 'r', encoding='UTF-8') as file:
    print(file.read())