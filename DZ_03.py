# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import random

#1
# list1 = [1, 0, 4, -1, 5, 3, 9, 11]
# print(list1)
# sum = 0
# for i in range(1, len(list1), 2):
#     if i % 2 == 1:
#         sum += list1[i]
# print(f'Сумма элементов на нечетных позициях = {sum}')


#2
# def sumOddIndex(list1):
#     sum = 0
#     for i in range(len(list1)):
#         if i % 2 != 0:
#             sum += list1[i]
#     print(f"Сумма элементов на нечетных позициях = {sum}")

# list1 = [2, 3, 5, 9, 3]
# sumOddIndex(list1)
# list1 = list(map(int, input("Введите числа через пробел:\n").split()))
# sumOddIndex(list1)


# 2.Напишите программу, которая найдёт произведение пар чисел списка 
# (CСписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# def mult_list(list1):
#     l = len(list1) // 2 + 1 if len(list1) % 2 != 0 else len(list1) // 2
#     work_list = [list1[i]*list1[len(list1) - i - 1] for i in range(l)]
#     print(work_list)

# list1 = [2, 3, 4, 5, 6]
# mult_list(list1)
# list1 = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_list(list1)


# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list1 = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = [round(i % 1, 2) for i in list1 if i % 1 != 0]
# print(max(new_list) - min(new_list))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
#     print(f"Число {num} в двоичной системе это {binum})

# s = ""
# n = int(input("Введите число:\n"))
# while n != 0:
#     s = str(n % 2) + s
#     n //=2
# print(f'Преобразованное число в двоичной системе = {s}')


# 5. Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)

# def NegaFibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = [0]
# userNumber = int(input('Введите число: '))
# for e in range(1, userNumber + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)

