class Queue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.front = 0
        self.back = capacity - 1
        self.MAX_QUEUE =capacity
        self.count = 0
