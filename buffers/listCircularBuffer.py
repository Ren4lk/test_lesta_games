from collections.abc import Collection
from typing import Iterator, Any


class ListCircularBuffer(Collection):
    def __init__(self, size: int) -> None:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer")
        self.buffer = [None] * size
        self.size = size
        self.count = 0
        self.pointer = 0

    def push(self, x: Any) -> None:
        if self.count == self.size:
            self.pop()
        self.buffer[(self.pointer + self.count) % self.size] = x
        self.count += 1

    def pop(self) -> Any:
        if self.count == 0:
            return None
        item = self.buffer[self.pointer]
        self.buffer[self.pointer] = None
        self.pointer = (self.pointer + 1) % self.size
        self.count -= 1
        return item

    def __contains__(self, x: Any) -> bool:
        return x in self.buffer

    def __iter__(self) -> Iterator:
        for i in range(self.count):
            yield self.buffer[(self.pointer + i) % self.size]

    def __len__(self) -> int:
        return self.count

    def __repr__(self) -> str:
        return f"ListCircularBuffer({self.buffer!r})"
