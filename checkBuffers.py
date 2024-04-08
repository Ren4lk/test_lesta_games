import buffers
import random
from time import perf_counter_ns as pc
from sys import getsizeof


def check_speed(buffer, operation, N):
    t0 = pc()
    for i in range(N):
        operation(buffer)
    return pc() - t0


def add_random(buffer):
    buffer.push(random.randint(0, 10000))


def pop_item(buffer):
    buffer.pop()


N = 10_000_000

dequeBuffer = buffers.DequeCircularBuffer(N)
listBuffer = buffers.ListCircularBuffer(N)

deque_addition_time = check_speed(dequeBuffer, add_random, N)
list_addition_time2 = check_speed(listBuffer, add_random, N)

print("Addition speed:")
print(f"DequeCircularBuffer time: {deque_addition_time / 1e9}")
print(f"ListCircularBuffer time: {list_addition_time2 / 1e9}")

print("\nBuffer size:")
print(f"DequeCircularBuffer size: {getsizeof(dequeBuffer.buffer)}")
print(f"ListCircularBuffer size: {getsizeof(listBuffer.buffer)}")

deque_pop_time = check_speed(dequeBuffer, pop_item, N)
list_pop_time = check_speed(listBuffer, pop_item, N)

print("\nPop speed:")
print(f"DequeCircularBuffer time: {deque_pop_time / 1e9}")
print(f"ListCircularBuffer time: {list_pop_time / 1e9}")

# Addition speed:
# DequeCircularBuffer time: 23.747684
# ListCircularBuffer time: 26.3042843

# Buffer size:
# DequeCircularBuffer size: 82500760
# ListCircularBuffer size: 80000056

# Pop speed:
# DequeCircularBuffer time: 7.8169389
# ListCircularBuffer time: 9.7740865

# Циклический буфер в основе которого лежит двунаправленная очередь работает быстрее, чем буфер, в основе которого
# лежит список, в силу того что в нем используются эффективные операции добавления и удаления в конец и начало коллекции.
# Также можно заметить что буффер с deque занимает больше памяти, это связано с тем, что он хранит ссылки на каждый узел,
# что и позволяет эффективно добавлять и удалять элементы в начало и конец.
