"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    counter = 1
    while True:
        if counter % 2 == 0:
            yield counter
        counter += 1
        if counter == 10:
            break


if __name__ == "__main__":
    even_gen = get_even_number()
    for i in even_gen:
        print(f"next(even_gen) -> {i}")
