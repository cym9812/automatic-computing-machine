class Stack:
    def __init__(self):
        self.a_stack = []
    def is_empty(self):
        if self.a_stack:
            return False
        else:
            return True
    def push(self, item):
        self.a_stack.append(item)
    def pop(self):
        return self.a_stack.pop()
    def peek(self):
        return self.a_stack[-1]
    def size(self):
        return len(self.a_stack)
    
def balanced_brackets(text):
    s = Stack()
    a_dict = {">":"<",")":"("}
    for i in text:
        if i == "(" or i == "<":
            s.push(i)
        elif i == ")" or i == ">":
            p = s.pop()
            if p != a_dict[i]:
                return "False"
    return s.is_empty()

print(balanced_brackets('x<y)(>z'))