class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_stack:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            if self.min_stack[-1] == self.stack.pop():
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1


minStack = MinStack()
minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.top()
minStack.getMin()