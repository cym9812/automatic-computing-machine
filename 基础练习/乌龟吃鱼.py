import abc
import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        print("鱼的初始位置:", self.x, self.y)

    def move(self):
        move_x = r.randrange(-1, 2, 2)
        move_y = r.randrange(-1, 2, 2)
        self.x = (self.x + move_x) % 10
        self.y = (self.y + move_y) % 10
        print("鱼的位置:", self.x, self.y)


class Turtle:
    def __init__(self):
        self.position_turtle_x = r.randint(0, 10)
        self.position_turtle_y = r.randint(0, 10)
        print('乌龟初始位置为：', self.position_turtle_x, self.position_turtle_y)

    def show_position(self):
        print('当前乌龟的位置为：', self.position_turtle_x, self.position_turtle_y)

    def move_turtle(self):
        move_turtle = input('请用wasd控制乌龟（一回合两次输入机会）：')
        if move_turtle == 'w':
            if self.position_turtle_y == 10:
                self.position_turtle_y = self.position_turtle_y - 1
            else:
                self.position_turtle_y = self.position_turtle_y + 1
        elif move_turtle == 'a':
            if self.position_turtle_x == 0:
                self.position_turtle_x = self.position_turtle_x + 1
            else:
                self.position_turtle_x = self.position_turtle_x - 1
        elif move_turtle == 's':
            if self.position_turtle_y == 0:
                self.position_turtle_y = self.position_turtle_y + 1
            else:
                self.position_turtle_y = self.position_turtle_y - 1
        elif move_turtle == 'd':
            if self.position_turtle_x == 10:
                self.position_turtle_x = self.position_turtle_x - 1
            else:
                self.position_turtle_x = self.position_turtle_x + 1
        self.show_position()
        return self.position_turtle_x, self.position_turtle_y

if __name__ == '__main__':
    f1 = Fish()
    f2 = Fish()
    f3 = Fish()
    f4 = Fish()
    f5 = Fish()
    fish = [f1,f2,f3,f4,f5]
    print("乌龟出现了！")
    turtle = Turtle()
    count = 0
    while fish:
        for i in fish:
            i.move()
        x,y = turtle.move_turtle()
        remain_fish = []
        for i in fish:
            if x == i.x and y == i.y:
                count += 1
                print("吃到鱼了！累计吃到%d条鱼了" %count)
                del i
            else:
                remain_fish.append(i)
        fish = remain_fish
        remain_fish = []
        x,y = turtle.move_turtle()
        for i in fish:
            if x == i.x and y == i.y:
                count += 1
                print("吃到鱼了！累计吃到%d条鱼了" %count)
                del i
            else:
                remain_fish.append(i)
        fish = remain_fish
