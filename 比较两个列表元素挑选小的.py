def get_list_of_minimums(list1, list2):
    number = 0
    list3 = []
    for element1 in list1:
        if element1 < list2[number]:
            list3.append(element1)
        else:
            list3.append(list2[number])
        number += 1
    return list3
list3 = get_list_of_minimums([3, 6, 9, 2], [1, 8, 5, 3])
print(list3)
