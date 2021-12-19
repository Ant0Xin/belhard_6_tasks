"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    f1 = 0
    f2 = 1
    for _ in range(6):
        f1, f2 = f2, f1 + f2
        yield f1


if __name__ == "__main__":
    fibonacci_gen = fibonacci(6)
    for i in fibonacci_gen:
        print(f"next(fibonacci_gen) -> {i}")
