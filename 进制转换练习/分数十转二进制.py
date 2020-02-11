import decimal

def fraction_to_binary(fraction_string, significant_binary_digits):
    result = []
    count_significant = 0
    count_total = 0
    s = False
    p = False
    fraction = decimal.Decimal(fraction_string)
    print(fraction)
    while count_significant <= significant_binary_digits:
        if fraction >= 1:
            fraction = fraction - 1
        fraction = fraction * 2
        if fraction >= 1:
            result.append(1)
            print(1, end=' ')
            s = True
        else:
            result.append(0)
            print(0, end=' ')
        if s:
            count_significant += 1
        count_total += 1
    print()
    #temp = 0
    index = count_total - 2
    if result[count_total - 1] == 1:
        temp = 1
        while temp == 1 and index >= 0:
            if result[index] == 1:
                result[index] = 0
            else:
                result[index] = 1
                temp = 0
            index -= 1
        if temp == 1:
            print('1.', end='')
            significant_binary_digits -= 1
            p = True
        else:
            print('0.', end='')
    else:
        print('0.', end='')
    count_print_significant = 0
    i = 0
    while count_print_significant < significant_binary_digits and i < 32:
        if result[i] == 1:
            p = True
        print(result[i], end='')
        i += 1
        if p:
            count_print_significant += 1
    print()

while True:
    value = str(input("fraction string: "))
    sign = int(input("significant binary digits: "))
    fraction_to_binary(value, sign)