import random


def main():
    introduction()
    user_input = str(get_user_input())
    computer_input = generate()
    judge(user_input, computer_input)


def introduction():
    print()
    print("#" * 14)
    print(" 剪刀~石头~布")
    print("#" * 14)
    print()


def get_user_input():
    user_input = input("请输入剪刀, 石头或布: ")
    return user_input


def generate():
    computer_input = random.choice(['剪刀', '石头', '布'])
    print("电脑选择出:", computer_input)
    print("-" * 18)
    return computer_input


def judge(user, computer):
    if user == computer:
        print("Draw")
    elif user == "剪刀":
        if computer == "石头":
            print("You lose")
        else:
            print("You win")
    elif user == "石头":
        if computer == "布":
            print("You lose")
        else:
            print("You win")
    elif user == "布":
        if computer == "剪刀":
            print("You lose")
        else:
            print("You win")

while True:
    main()
