# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь 
# в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# Ввод: 5
# Ввод: 1 5 3 4 2
# Ввод: 3
# -> 1

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
x = int(input())
count = 0
for el in a:
    if el == x:
        count +=1
print(count)