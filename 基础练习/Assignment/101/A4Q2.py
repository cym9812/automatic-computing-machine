def print_most_numbers_occurrences(numbers_str):
    numbers = {}
    result = []
    most_number = 0
    numbers_list = numbers_str.split()
    for number in numbers_list:
        numbers[number] = numbers_list.count(number)
    for number1 in numbers:
        if numbers[number1] > most_number:
            most_number = numbers[number1]
    for number2 in numbers:
        if numbers[number2] == most_number:
            result.append(number2)
    for i in result:
        print(i, end=' ')
    print()

print_most_numbers_occurrences('2 3 40 1 5 4 3 3 9 9')
print_most_numbers_occurrences('9 30 3 9 3 1 4')
