from time import perf_counter_ns as pc
import random


def isEven(value):
    return value % 2 == 0


def isEvenFaster(value):
    return value & 1 == 0


def checkParityFunctions(n, fun):
    t0 = pc()
    result = fun(n)
    time_check = pc() - t0
    return result, time_check


if __name__ == "__main__":
    n = random.randint(0, 10_000_000_000)
    mod_result, mod_time_check = checkParityFunctions(n, isEven)
    byte_and_result, byte_and_time_check = checkParityFunctions(n, isEvenFaster)

    assert mod_result == byte_and_result

    print(f"mod time: {mod_time_check / 1e3}")
    print(f"& time: {byte_and_time_check / 1e3}")

# mod time: 6.4
# & time: 5.0

# Вариант с логическим и быстрее в силу работы с самими битами числа, и отсутствием вычисления "дорогой" операции деления.
# Но такой вариант требует немного больше времени для понимания что происходит читателю
