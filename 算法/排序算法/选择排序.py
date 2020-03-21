def my_selection_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        position_largest = 0
        for i in range(1, pass_num + 1):
            if a_list[i] > a_list[position_largest]:
                position_largest = i
        swap_elements(a_list, position_largest, pass_num)
        print(pass_num, "-", a_list)


def swap_elements(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]

def selection_sort(a_list):
    for curr in range(len(a_list)):
        low = curr
        for i in range(curr + 1, len(a_list)):
            if a_list[i] < a_list[low]:
                low = i
        a_list[curr], a_list[low] = a_list[low], a_list[curr]
        print(a_list)


a_list = [54, 26, 93, 17, 17, 31, 44, 55, 20]
print("\nSorting a list with Selection Sort")
print("before: ", a_list)
selection_sort(a_list)
print("after:  ", a_list)