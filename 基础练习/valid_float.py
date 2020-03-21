def valid_float(number_string):
    if '-' in number_string:
        if number_string.count('-') > 1:
            return False
        if number_string[0] != '-':
            return False
        pass
    if '+' in number_string:
        return False
    if number_string[0] == '0':
        if number_string[1] != '.':
            return False
    if '.' in number_string:
        if number_string.count('.') > 1:
            return False
        elif number_string[-1] == '.' or number_string[0] == '.':
            return False
        pass
    return True

def check(num_string):
    print(num_string, end=' is ')
    if not valid_float(num_string):
        print(end='not ')
    print('valid')

test_values = "1234 -1234 +123 123. 12.4 0.6 00.6 .6 -12.4 -0.6 -1234567890.123456789 12-.6335".split()
for number in test_values:
    check(number)