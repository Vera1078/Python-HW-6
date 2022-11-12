# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print('Произведение пар чисел списка')
from random import randint

number = int(input('Введите размер списка: '))
list1 = []
list2 = []

# for i in range(number):
#     list1.append(randint(0, 9))

list1 = list(map(lambda x: randint (0, 9), range (number)))

# for j in range((len(list1) + 1) // 2):
#     list2.append(list1[j] * list1[-(j + 1)])

list2 = list(map(lambda j: (list1[j] * list1[-(j + 1)]), range((len(list1) + 1) // 2) ))
        
print(f'Исходный список {list1}')
print(f'Произведение пар чисел списка {list2}')


