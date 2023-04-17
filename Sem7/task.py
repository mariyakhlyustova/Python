# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# list_1 = [56, 7, 98, 456, 3, -98]
# list_1 = list(filter(lambda x: 9 < abs(x) < 100, list_1))
# print(list_1)

# 2) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = input()
# print(n)
# list_1 = list(filter(lambda x: x.isnumeric(), n))
# print(list_1)
# list_1 = sum(list(map(int, list_1)))
# print(list_1)

num = [23, 4, '4', 'dsfs', 0.45, 'zxzxz']
# print(num)

spis1 = list(filter(lambda x: type(x) != str, num))
spis2 = list(filter(lambda x: type(x) == str, num))

print(spis1, spis2)