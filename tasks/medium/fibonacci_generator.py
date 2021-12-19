"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num):
    f1, f2 = 1, 1
    if num < 1:
        raise ValueError('Введите значение больше 1')
    for i in range(num):
        yield f1
        f1, f2 = f2, f1 + f2


fibonacci_gen = fibonacci(5)
for i in fibonacci_gen:
    print(i)
