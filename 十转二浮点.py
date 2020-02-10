def float_string_to_binary(float_string):
    result = []
    count = 0
    if float(float_string) == 0:
        print('0 0000 00000000000')
    else:
        if float_string[0] != '-':
            print('0', end=' ')
        else:
            print('1', end=' ')
            float_string = float_string[1:]
        if '.' in float_string:
            integer, fraction = float_string.split('.')
            fraction = float('0.' + fraction)
            integer = int(integer)
            while count < 24:
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
            integer = int(float_string)
            result.append('.')
        if integer == 0:
            result.insert(0, '0')
        else:
            while integer != 0:
                i = integer % 2
                if i != 0:
                    result.insert(0, '1')
                else:
                    result.insert(0, '0')
                integer = integer // 2
        a = result.index('.')
        b = result.index('1') + 1
        result.remove('.')
        exponent = a - b + 7
        if b > a:
            exponent += 1
        exponent_binary = []
        index = b + 10
        while len(result) <= 24:
            result.append('0')
        if result[b + 11] == '1':
            temp = 1
            while temp == 1 and index >= 0:
                if result[index] == '1':
                    result[index] = '0'
                else:
                    result[index] = '1'
                    temp = 0
                index -= 1
            if temp == 1:
                result[0] = '0'
                result.insert(0, '1')
                exponent += 1
        while exponent != 0:
            i = exponent % 2
            if i != 0:
                exponent_binary.insert(0, '1')
            else:
                exponent_binary.insert(0, '0')
            exponent = exponent // 2
        while len(exponent_binary) < 4:
            exponent_binary.insert(0, '0')
        for i in exponent_binary:
            print(i, end='')
        print(' ', end='')
        start_print = False
        count_print = 0
        item = 0
        while count_print < 11:
            if not start_print:
                if result[item] == '1':
                    start_print = True
            else:
                print(result[item], end='')
                count_print += 1
            item += 1
        print()



while True:
    value = str(input("Decimal: "))
    float_string_to_binary(value)