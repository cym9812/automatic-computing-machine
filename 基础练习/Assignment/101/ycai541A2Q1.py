"""
Name: Yimeng Cai
username: ycai541
ID number: 455251836
Description: A program that fulfills the functionalities of a mathematical
quiz with the five basic arithmetic operations, i.e., addition, subtraction,
multiplication, integer division and modulo operation
"""
import random


def main():
    display_intro()
    display_menu()
    display_separator()
    option = get_user_input()
    total = 0
    correct = 0
    while option != 6:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()
    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)


def display_intro():
    print("*" * 24)
    print("** A Simple Math Quiz **")
    print("*" * 24)


def display_menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Integer Division")
    print("5. Modulo Operation")
    print("6. Exit")


def display_separator():
    print("-" * 24)


def get_user_input():
    option = int(input("Enter your choice: "))
    while option > 6:
        print("Invalid menu option.")
        option = int(input("Please try again: "))
    return option


def get_user_solution(problem):
    print("Enter your answer")
    answer = int(input(problem))
    return answer


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        print("Correct.")
        count = count + 1
        return count
    else:
        print("Incorrect.")
        return count


def menu_option(index, count):
    number1 = random.randrange(1, 31)
    number2 = random.randrange(1, 31)
    if index == 1:
        solution = number1 + number2
        problem = str(number1) + " + " + str(number2) + " = "
    elif index == 2:
        solution = number1 - number2
        problem = str(number1) + " - " + str(number2) + " = "
    elif index == 3:
        solution = number1 * number2
        problem = str(number1) + " * " + str(number2) + " = "
    elif index == 4:
        solution = number1 // number2
        problem = str(number1) + " // " + str(number2) + " = "
    else:
        solution = number1 % number2
        problem = str(number1) + " % " + str(number2) + " = "
    user_solution = get_user_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count


def display_result(total, correct):
    if total == 0:
        print("You answered 0 questions with 0 correct.")
        print("Your score is 0%. Thank you.")
    else:
        percentage = correct / total * 100
        percentage = round(percentage, 2)
        print("You answered", total, "questions with", correct, "correct.")
        print("Your score is ", percentage, "%. Thank you.", sep="")

main()
