######################################
#   COMPSCI 105 S2 C, 2017           #
#   Assignment 1 Question 2          #
#                                    #
#   @author:     Yimeng Cai, Ycai541 #
#   @version:    04/09/2017          #
######################################

class Stack:
    def __init__(self):
        self.a_stack = []
    def is_empty(self):
        return len(self.a_stack) == 0
    def push(self, item):
        self.a_stack.append(item)
    def pop(self):
        return self.a_stack.pop()
    def peek(self):
        return self.a_stack[-1]
    def size(self):
        return len(self.a_stack)

def q2(text):
    operators = {'>' : 5, '<' : 5, '+' : 4, '-' : 4, '*' : 3, '/' : 3, '^' : 2, '(' : 1, ')' : 1}
    number = ""
    stack = Stack()
    result = []
    text = text.replace(" ", "")
    for i in text:
        if i not in operators.keys():
            number += i
        else:
            if number != '':
                result.append(number)
                number = ''
            if not stack.is_empty():
                if i == '(':
                    stack.push(i)
                elif i == ')':
                    while not stack.peek() == '(':
                        result.append(stack.pop())
                    stack.pop()
                else:
                    if stack.peek() == '(':
                        stack.push(i)
                    elif operators[i] > operators[stack.peek()]:
                        result.append(stack.pop())
                    elif operators[i] == operators[stack.peek()]:
                        result.append(stack.pop())
                        stack.push(i)
                    else:
                        stack.push(i)
            else:
                stack.push(i)
    if number != '':
        result.append(number)
    while not stack.is_empty():
        result.append(stack.pop())
    print(result)
    return evaluate_postfix(result)

def evaluate_postfix(text):
    s = Stack()
    operator = ['^', '+', '-', '*', '/', '<', '>']
    for i in text:
        if i not in operator:
            s.push(i)
        else:
            a = s.pop()
            b = s.pop()
            c = compute(b, a, i)
            s.push(c)
    return s.pop()

def compute(num1, num2, operator):
    if operator == '+':
        return int(num1) + int(num2)
    elif operator == '-':
        return int(num1) - int(num2)
    elif operator == '*':
        return int(num1) * int(num2)
    elif operator == '/':
        return int(num1) / int(num2)
    elif operator == '^':
        return int(num1) ** int(num2)
    elif operator == '<':
        return min(int(num1), int(num2))
    elif operator == '>':
        return max(int(num1), int(num2))


if __name__ == '__main__':
    print(q2(input()))
