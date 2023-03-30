# n = int(input())
# multi = 1
# while n > 1:
#     multi *= n
#     n -= 1
# print(multi)
# -----------------------------------------
# a = int(input())
# startA = a
# n = 3
# f = 1.618
# while a > 2:
#     a = a / f
#     n += 1
# fib = round((f**n -(1-f)**n) / 5 **0.5)
# if fib == startA:
#     print(n + 1)
# else:
#     print(-1)

# a = int(input('Введите целое число больше 1: '))
# if a == 0:
#     print(0)
# else:
#     fib_prev, fib_next = 0, 1
#     n = 1
#     while fib_next <= a:
#         if fib_next == a:
#             print(n + 1)
#             break
#         fib_prev, fib_next = fib_next, fib_prev + fib_next
#         n += 1
#     else:
#         print(-1)
# -----------------------------------------
# n = int(input())
# min = 1000000
# while n > 0:
#     a = int(input())
#     if a < min:
#         min = a
#     n -= 1
# print(min)
# -----------------------------------------
# n = int(input())
# maxcount = 0
# count = 0
# while n > 0:
#     a = int(input())
#     if a > 0:
#         count += 1
#     else:
#         if count > maxcount:
#             maxcount = count
#         count = 0
#     n -= 1
# print(maxcount)