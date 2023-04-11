# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# ввод оценок пока != 0

list_1 = list()

def marks (somelist_1):
    while True:
        a = int(input("Введите оценку "))
        if a == 0:
            break
        somelist_1.append(a)
    return somelist_1

def cm (somelist_2):
    maxmark = max(somelist_2)
    minmark = min(somelist_2)
    for i in range(len(somelist_2)):
        if somelist_2[i] == maxmark:
            somelist_2[i] = minmark
    return somelist_2

print(marks(list_1))
print(cm(list_1))

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
n = int(input("Введите число: "))

def simple(a):
    for i in range(2,a):
        if a%i==0:
            return "No"
        else:
            return "Yes"
        
print(simple(n))


# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# При помощи рекурсии

# 5
# (n):
# 1
# 2
# 3
# 4
# 5
# 5 4 3 2 1

n = int(input("Введите число: "))

def somefunc (a):
    result = str(a)
    if a == 1:
        return result
    return result + somefunc(a-1)

print(somefunc(n))