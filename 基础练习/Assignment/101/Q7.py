def get_hand_score(list_of_dice):
    list_of_dice.sort()
    score = 0
    number = 2
    if 1 not in list_of_dice:
        return 0
    else:
        while 1 in list_of_dice:
            list_of_dice.remove(1)
            score += 1
            while number in list_of_dice:
                score += number
                list_of_dice.remove(number)
                number += 1
            number = 2
        return score


def main():
    print(get_hand_score([5, 3, 2, 5, 5, 6, 4, 3]))
    print(get_hand_score([3, 4, 1, 5, 3, 1, 4, 6]))
    print(get_hand_score([5, 3, 2, 6, 4, 5, 1, 4]))
    print(get_hand_score([2, 1, 1, 1, 2, 3, 3, 2]))

main()