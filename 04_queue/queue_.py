
class ArrayQueue:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__itmes = [None] * capacity
        self.__head = 0
        self.__tail = 0

    def __repr__(self):
        return str(self.__itmes[self.__head:self.__tail])

    def __len__(self):
        return self.__tail - self.__head

    def enqueue(self, value: int) -> bool:
        """
        均摊时间复杂度：O(1)
        """
        if self.__head == 0 and self.__tail == self.__capacity:
            return False
        if self.__head != 0 and self.__tail == self.__capacity:
            for i in range(self.__head, self.__tail, 1):
                self.__itmes[i - self.__head] = self.__itmes[i]
            self.__tail = self.__tail - self.__head
            self.__head = 0

        self.__itmes[self.__tail] = value
        self.__tail += 1
        return True

    def dequeue(self) -> int:
        """
        时间复杂度: O(1)
        """
        if self.__head == self.__tail:
            return None

        value = self.__itmes[self.__head]
        self.__head += 1
        return value


class DynamicArrayQueue(object):
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__items = [None] * capacity
        self.__head = 0
        self.__tail = 0
        self.__factor = 2

    def __repr__(self):
        return str(self.__items[self.__head:self.__tail])

    def __len__(self):
        return self.__tail - self.__head

    def __extend(self):
        capacity = self.__capacity * self.__factor
        new_items = [None] * capacity
        for i in range(self.__capacity):
            new_items[i] = self.__items[i]
        self.__items = new_items
        self.__capacity = capacity

    def enqueue(self, value: int):
        if self.__head == 0 and self.__tail == self.__capacity:
            self.__extend()
        elif self.__head != 0 and self.__tail == self.__capacity:
            for i in range(self.__head, self.__tail, 1):
                self.__itmes[i - self.__head] = self.__itmes[i]
            self.__tail = self.__tail - self.__head
            self.__head = 0
        self.__items[self.__tail] = value
        self.__tail += 1
        return True

    def dequeue(self):
        if self.__head == self.__tail:
            return None

        value = self.__items[self.__head]
        self.__head += 1
        return value


class Node(object):
    def __init__(self, data: int, next: 'Node' = None):
        self.data = data
        self.next = next


class LinkedListQueue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __iter__(self):
        p = self.__head
        while p:
            yield p.data
            p = p.next

    def __repr__(self):
        return " -> ".join((str(i) for i in self))

    def enqueue(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            self.__tail.next = new_node
        self.__tail = new_node

    def dequeue(self) -> int:
        if self.__head is None:
            return None
        value = self.__head.data
        self.__head = self.__head.next
        return value


class CircularQueue(object):
    def __init__(self, capacity: int):
        # 额外多出一个存储，用于判断是否队满
        self.__capacity = capacity + 1
        self.__items = [None] * self.__capacity
        self.__head = 0
        self.__tail = 0

    def __iter__(self):
        p = self.__head
        while p != self.__tail:
            yield self.__items[p]
            p = (p + 1) % self.__capacity

    def __repr__(self):
        return str(list(self))

    def enqueue(self, value: int) -> bool:
        # 判断队满
        if (self.__tail + 1) % self.__capacity == self.__head:
            return False
        self.__items[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__capacity
        return True

    def dequeue(self):
        if self.__head == self.__tail:
            return None
        value = self.__items[self.__head]
        self.__head = (self.__head + 1) % self.__capacity
        return value


class CircularQueueV2(object):
    """
    循环队列，不牺牲存储空间的实现方式
    """
    def __init__(self, capacity: int):
        # 额外多出一个存储，用于判断是否队满
        self.__capacity = capacity
        self.__items = [None] * capacity
        self.__size = 0
        self.__head = 0
        self.__tail = 0

    def __iter__(self):
        for i in range(self.__size):
            p = (self.__head + i) % self.__capacity
            yield self.__items[p]

    def __repr__(self):
        return str(list(self))

    def enqueue(self, value: int) -> bool:
        # 判断队满
        if self.__tail == self.__head and self.__size == self.__capacity:
            return False
        self.__items[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__size += 1
        return True

    def dequeue(self):
        if self.__size == 0:
            return None
        value = self.__items[self.__head]
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1
        return value
