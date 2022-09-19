def write_array(array, file_name):
    file_name.write('\n'.join(array))
    
array = ['Топ коктейльных баров Москвы:','Noor Electro','Do Not Disturb','Dictatura','Ботанист','Вермутерия']

with open('task_2.txt', 'w', encoding='UTF-8') as file:
    write_array(array, file)

with open('task_2.txt', 'r', encoding='UTF-8') as file1: 
    print(file1.read())