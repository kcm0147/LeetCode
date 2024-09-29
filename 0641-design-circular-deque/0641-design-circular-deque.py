from collections import defaultdict
from typing import List, Set


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = []
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size < self.k:
            self.queue.insert(0, value)
            self.size = len(self.queue)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.k:
            self.queue.insert(self.size, value)
            self.size = len(self.queue)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size > 0:
            self.queue.pop(0)
            self.size = len(self.queue)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.queue.pop()
            self.size = len(self.queue)
            return True
        return False

    def getFront(self) -> int:
        if self.size > 0:
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        if self.size > 0:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
