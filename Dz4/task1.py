# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input())
list_1 = []
for i in range(n):
    list_1.append(int(input()))

m = int(input())
list_2 = []
for i in range(m):
    list_2.append(int(input()))

set_1 = set(list_1)
set_2 = set(list_2)
set_inter = set_1.intersection(set_2)
list_0 = list(set_inter)
print(sorted(list_0))