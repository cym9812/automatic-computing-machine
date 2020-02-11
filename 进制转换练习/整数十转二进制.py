def integer_to_binary(value):
    result = []
    value = int(value)
    if value == 0:
        print(0)
        print(0)
    else:
        while value != 0:
            i = value % 2
            if i != 0:
                print(1, end=' ')
                result.append(1)
            else:
                print(0, end=' ')
                result.append(0)
            value = value // 2
        print()
        result.reverse()
        for each in result:
            print(each, end='')
        print()

test_values = '0 10 100 65535 65536 9903520314283042199192993792'.split()
for value in test_values:
    print('Decimal:', value)
    integer_to_binary(value)
