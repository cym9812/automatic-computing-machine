def get_morse_code_dict(filename):
    morse = {}
    file = open(filename, "r")
    for each_line in file:
        morse[each_line[0]] = each_line[2:-1]
    file.close()
    return morse
