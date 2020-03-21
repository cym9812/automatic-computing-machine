def order_weight(number):
    number_list = number.split()
    digits_sum = []
    number_and_digits = {}
    result = []
    number_order = 0
    result_str = ""
    for number in number_list:
        for i in number:
            number_order += int(i)
        number_order += int(number) / (10 ** len(str(number)))
        digits_sum.append(number_order)
        number_order = 0
    for i in range(0, len(digits_sum)):
        number_and_digits[digits_sum[i]] = number_list[i]
    digits_sum.sort()
    for i in digits_sum:
        result.append(number_and_digits[i])
    for i in result:
        result_str += str(i) + " "
    return result_str


def main():
    print(order_weight("56 65 74 100 99 68 86 180 90"))

main()
