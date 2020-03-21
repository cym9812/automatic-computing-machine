def main():
    list1 = [-1, 2, -3]
    list2 = [4, -6, 3]
    print("1.", get_negatives_at_front(list1, list2))
    print("2.", get_negatives_at_front([1, 2, -3, 4, 7], [4, -6, 3, -1]))
    print("3.", get_negatives_at_front([-1, -2, 6], [-5, 1, 2]))
    print("4.", get_negatives_at_front([], []))


def get_negatives_at_front(list1, list2):
    if list1 or list2:
        count = 0
        positive = []
        negative = []
        while count < len(list1) and count < len(list2):
            if list1[count] > 0:
                positive = [list1[count]] + positive
            else:
                negative = negative + [list1[count]]
            if list2[count] > 0:
                positive = [list2[count]] + positive
            else:
                negative = negative + [list2[count]]
            count += 1
        while count < len(list1):
            if list1[count] > 0:
                positive = [list1[count]] + positive
            else:
                negative = negative + [list1[count]]
            count += 1
        while count < len(list2):
            if list2[count] > 0:
                positive = [list2[count]] + positive
            else:
                negative = negative + [list2[count]]
            count += 1
        return negative + positive

    else:
        return []
main()
