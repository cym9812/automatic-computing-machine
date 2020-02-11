class Squares:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
        self.current = 0
        self.sqr = self.current * self.current
        self.result = []
        while self.sqr <= self.b:
            if self.sqr < self.a:
                self.current += 1
            else:
                self.current += 1
                self.result.append(self.sqr)
            self.sqr = self.current * self.current
        self.result.reverse()

    def __iter__(self):
        return self

    def __next__(self):
        if self.result != []:
            return self.result.pop()
        elif self.sqr > self.b:
            raise StopIteration()

s = Squares(5, 50)
for i in s:
    print(i)
