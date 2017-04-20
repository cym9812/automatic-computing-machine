def main():
    number = get_user_input()
    number_type = odd_or_even_number(number)
    if number == 0:
        print("error")
    elif number_type == "odd":
        result = odd_number(number)
        print(result)
    else:
        result = even_number(number)
        print(result)


def get_user_input():
    number = int(input("input = "))
    return number


def odd_or_even_number(number):
    if number % 2 > 0:
        return "odd"
    else:
        return "even"


def odd_number(number):
    result = 1
    while number > 1:
        result = result + 1 / number
        number -= 2
    return result


def even_number(number):
    result = 1 / 2
    while number > 2:
        result = result + 1 / number
        number -= 2
    return result

while True:
    main()
