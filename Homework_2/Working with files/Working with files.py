# Создаем файл sample.txt
with open('sample.txt', 'w') as file:
    file.write('Hello World!')

# Читаем содержимое файла и выводим на экран
with open('sample.txt') as file:
    print(file.read())
