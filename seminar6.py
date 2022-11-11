# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

print('Задача на вывод списка из n чисел последовательности (1+1/n)^n и их суммы')
n = int(input("Введите целое положительное число: "))
numbers = {n : round(pow((1 + 1 / n), n), 2) for n in range(1, n + 1)}

val_sum = 0
for j in numbers.values():
    val_sum += j

# sum = lambda x : x for j in numbers.values() val_sum += x)

print(f'Для n = {n} {numbers}')
print(f'Сумма значений = {round(val_sum, 2)}')

print()
print()