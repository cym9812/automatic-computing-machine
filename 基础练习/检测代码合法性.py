def main():
    print("1.", is_legitmate_code('B747346'))
    print("2.", is_legitmate_code('X  444  454'))
    print("3.", is_legitmate_code('T 444854'))
    print("4.", is_legitmate_code('X  444X454'))
    print("5.", is_legitmate_code('X  '))
    print("6.", is_legitmate_code('C123  '))
    print("6.", is_legitmate_code('   '))


def is_legitmate_code(string):
    code_letters = ["A", "B", "Z", "T", "X"]
    min_for_each_letter = [2, 2, 1, 0, 4]
    max_for_each_letter = [8, 9, 6, 7, 5]
    string = string.replace(" ", "")
    count = 0
    if string != "" and len(string) > 1:
        if string[0] in code_letters:
            if string[1:].isdigit():
                if string[0] == "A":
                    for number in string[1:]:
                        if min_for_each_letter[0] <= int(number) <= max_for_each_letter[0]:
                            count = count + 1
                    if count == len(string) - 1:
                        return "True"
                    else:
                        return "False"
                elif string[0] == "B":
                    for number in string[1:]:
                        if min_for_each_letter[1] <= int(number) <= max_for_each_letter[1]:
                            count = count + 1
                    if count == len(string) - 1:
                        return "True"
                    else:
                        return "False"
                elif string[0] == "Z":
                    for number in string[1:]:
                        if min_for_each_letter[2] <= int(number) <= max_for_each_letter[2]:
                            count = count + 1
                    if count == len(string) - 1:
                        return "True"
                    else:
                        return "False"
                elif string[0] == "T":
                    for number in string[1:]:
                        if min_for_each_letter[3] <= int(number) <= max_for_each_letter[3]:
                            count = count + 1
                    if count == len(string) - 1:
                        return "True"
                    else:
                        return "False"
                elif string[0] == "X":
                    for number in string[1:]:
                        if min_for_each_letter[4] <= int(number) <= max_for_each_letter[4]:
                            count = count + 1
                    if count == len(string) - 1:
                        return "True"
                    else:
                        return "False"
            else:
                return "False"
        else:
            return "False"
    else:
        return "False"

main()
