def main():
    a_list = [6, 6, 6, 7, 6, 6, 4, 3, 3, 3, 8, 8, 8, 3]
    remove_triples(a_list)
    print("1.", a_list)
    a_list = [1, 1, 1, 4, 4, 4, 1, 1, 1]
    remove_triples(a_list)
    print("2.", a_list)
    a_list = [1, 1, 1, 1, 1, 2]
    remove_triples(a_list)
    print("3.", a_list)


def remove_triples(a_list):
    count = 0
    if a_list:
        if len(a_list) >= 3:
            result = a_list[0:2]
            for number in a_list[2:]:
                if number != result[-1] or number != result[-2]:
                    result.append(number)
            for i in result:
                while a_list[count] != i:
                    del a_list[count]
                count += 1
            if a_list[-1] == a_list[-2] == a_list[-3]:
                del a_list[-1]


main()
