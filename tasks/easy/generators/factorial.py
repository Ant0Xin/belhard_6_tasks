"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    num_1 = 1
    num_2 = 1
    for _ in range(4):
        num_2 *= num_1
        yield num_2
        num_1 += 1


if __name__ == "__main__":
    factorial_gen = factorial(4)
    for i in factorial_gen:
        print(f"next(factorial_gen) -> {i}")
