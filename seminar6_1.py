 
# Задача 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]


print('Список неповторяющихся элементов исходной последовательности') 
print('Введите числа через пробел')
list1 = list (map(int, input().split()))
list2 = []

# for i in list1:
#if list1.count (i) ==1:
#  list2.append(i)

list2 = list(filter(lambda x: list1.count (x) == 1, list1))
print(list2)
