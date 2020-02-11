def print_binary(number_string, fraction_length):
    result = []
    count = 0
    if number_string == '0':
        print('+0.' + '0' * fraction_length)
    else:
        if number_string[0] != '-':
            print('+', end='')
        else:
            print('-', end='')
            number_string = number_string[1:]
        if '.' in number_string:
            integer, fraction = number_string.split('.')
            fraction = float('0.' + fraction)
            integer = int(integer)
            while count < fraction_length:
                fraction = fraction * 2
                if fraction >= 1:
                    result.append('1')
                else:
                    result.append('0')
                if fraction >= 1:
                    fraction = fraction - 1

                count += 1
            result.insert(0, '.')
        else:
            integer = int(number_string)
            result.append('.')
            result.append('0' * fraction_length)
        if integer == 0:
            result.insert(0, 0)
        else:
            while integer != 0:
                i = integer % 2
                if i != 0:
                    result.insert(0, '1')
                else:
                    result.insert(0, '0')
                integer = integer // 2
        for each in result:
            print(each, end='')
        print()

test_values = "0 1234 -1234 12.4 0.6 -12.4 -0.6 -1234567890.123456789".split()
for number in test_values:
    print(number, end=': ')
    print_binary(number, 10)