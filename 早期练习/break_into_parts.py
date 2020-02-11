def break_into_parts(decimal_string):
    if decimal_string[0] != '-':
        print('sign: + ', end='')
    else:
        print('sign: - ', end='')
        decimal_string = decimal_string[1:]
    if '.' in decimal_string:
        result = decimal_string.split('.')
        print('integer:', result[0], 'fraction:', result[1])
    else:
        print('integer:', decimal_string, 'fraction: 0')