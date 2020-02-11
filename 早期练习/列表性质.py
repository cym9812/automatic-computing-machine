def fiddle_lists (list1, list2):
    list1 = [1, 5]
    list2.append(list1[1])
    list1.append(list2[0])
    list1.append (list2 [1])
def main():
    a_list1 = [5, 3, 2]
    a_list2 = [4, 6]
    fiddle_lists(a_list1, a_list2)
    print("a list1:", a_list1)
    print("a list2:", a_list2)
main ()
