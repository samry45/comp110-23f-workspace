from __future__ import annotations

class Node:

    data: int
    next: Node

    def __init__(self, data: int, next: Node):
        self.data = data
        self.next = next