import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def move(self):
        move_direction = r.randrange(-1, 2, 2)
        move_direction2 = r.randrange(-1, 2, 2)
        if move_direction > 0:
            self.x = self.x + move_direction2
            if self.x < 0:
                self.x = - self.x
            if self.x > 10:
                self.x = 9
        else:
            self.y = self.y + move_direction2
            if self.y < 0:
                self.y = - self.y
            if self.y > 10:
                self.y = 9
        print("position:", self.x, self.y)

class Turtle:
    def __init__(self):
        self.position_turtle_x = r.randint(0, 10)
        self.position_turtle_y = r.randint(0, 10)
        print('乌龟生成位置为：', self.position_turtle_x, self.position_turtle_y)

    def move_turtle(self):
        number_of_move = 0
        while number_of_move < 2:
            number_of_move += 1
            move_turtle = input('请用wasd控制乌龟（一回合两次输入机会）：')
            if move_turtle == 'w':
                if self.position_turtle_y == 10:
                    self.position_turtle_y = self.position_turtle_y - 1
                else:
                    self.position_turtle_y = self.position_turtle_y + 1
            if move_turtle == 'a':
                if self.position_turtle_x == 0:
                    self.position_turtle_x = self.position_turtle_x + 1
                else:
                    self.position_turtle_x = self.position_turtle_x - 1
            if move_turtle == 's':
                if self.position_turtle_y == 0:
                    self.position_turtle_y = self.position_turtle_y + 1
                else:
                    self.position_turtle_y = self.position_turtle_y - 1
            if move_turtle == 'd':
                if self.position_turtle_x == 10:
                    self.position_turtle_x = self.position_turtle_x - 1
                else:
                    self.position_turtle_x = self.position_turtle_x + 1
            print('当前乌龟的位置为：', self.position_turtle_x, self.position_turtle_y)

class
