def main():
    matrix = get_input()
    count_line = 0
    count_row = 0
    line = locals()
    row = locals()
    for each_line in matrix:
        line["L" + str(count_line)] = matrix.readline().split()
        count_line += 1
    count_row = len(L1)
    temp = count_line
    while count_line != 0:
        for each_row in line["L" + str(count_line)]:
            row["R" + str(count_row)] = row["R" + str(count_row)] + each_row[count_row]
            count_line -= 1


def get_input():
    file_name = str(input("文件名: ")) + ".txt"
    matrix = open(file_name)
    return matrix

main()