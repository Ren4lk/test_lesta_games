from collections.abc import Collection
from collections import deque
from typing import Iterator, Any


class DequeCircularBuffer(Collection):
    def __init__(self, size: int) -> None:
        self.buffer = deque(maxlen=size)

    def push(self, x: Any) -> None:
        self.buffer.append(x)

    def pop(self) -> Any:
        if len(self.buffer) == 0:
            return None
        return self.buffer.popleft()

    def __contains__(self, x: Any) -> bool:
        return x in self.buffer

    def __iter__(self) -> Iterator:
        return iter(self.buffer)

    def __len__(self) -> int:
        return len(self.buffer)

    def __repr__(self) -> str:
        return f"DequeCircularBuffer({self.buffer!r})"
