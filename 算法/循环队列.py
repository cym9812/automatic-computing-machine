class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.que = [None] * k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            self.que[self.tail] = value
            self.tail = (self.tail + 1) % self.k
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.que[self.head] = None
            self.head = (self.head + 1) % self.k
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.que[self.head] if self.que[self.head] is not None else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.que[self.tail - 1] if self.que[self.tail - 1] is not None else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.que[self.head] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.head == self.tail and self.que[self.head] is not None


circularQueue = MyCircularQueue(3)
circularQueue.enQueue(1)
circularQueue.enQueue(2)
circularQueue.enQueue(3)
circularQueue.enQueue(4)
circularQueue.Rear()
circularQueue.isFull()
circularQueue.deQueue()
circularQueue.enQueue(4)
circularQueue.Rear()
