"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_1: list):
    compare_list = []
    for i in list_1:
        if i not in compare_list:
            print("No")
            compare_list.append(i)
        else:
            print("Yes")


yes_or_no([2, 6, 37, 2, 2, 8, 0, 9, 1, 6])
