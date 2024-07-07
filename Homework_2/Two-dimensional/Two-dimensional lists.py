# Создаем двумерный массив размером 3x3
array = [[0 for _ in range(3)] for _ in range(3)]

# Заполняем массив числами от 1 до 9
for i in range(3):
    for j in range(3):
        array[i][j] = i * 3 + j + 1

# Выводим строки массива
for row in array:
    print(' '.join(map(str, row)))
