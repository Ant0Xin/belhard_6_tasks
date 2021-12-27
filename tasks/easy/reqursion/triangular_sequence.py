"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, a=1, b=''):
    b += str(a) * a + '\n'
    if a != n:
        return triangular_sequence(n, a + 1, b)
    return b
