positiontoascii = {(1, 1): "1101", (1, 3): "1100", (3, 1): "1001", (3, 3): "1000", (-1, -1): "0111", (-1, -3): "0110",
                   (-3, -1): "0011", (-3, -3): "0010", (1, -1): "1111", (1, -3): "1110", (3, -1): "1011",
                   (3, -3): "1010", (-1, 1): "0101", (-1, 3): "0100", (-3, 1): "0001", (-3, 3): "0000"}
asciitoposition = {}
for each in positiontoascii.keys():
    asciitoposition[positiontoascii[each]] = each

def main():
    if int(input("模式：1.数字转位置  2.位置转数字")) == 1:
        if int(input("模式：1.从数字转换  2.从文件转换")) == 1:
            numbers = str(input("数字："))
            ascii_number = ""
            for i in numbers:
                temp = bin(ord(i))
                temp = temp[2:]
                while len(temp) < 8:
                    temp = "0" + temp
                ascii_number += temp
            result = ascii_to_position(ascii_number)
        else:
            file = open("number.txt","r")
            data = file.read().strip()
            result = ascii_to_position(data)
        print(result)
    else:
        file = open("position.txt", "r")
        data = file.readlines()
        a = find_position(data)
        b = find_nearest(find_position(data))
        i = 0
        while i < len(a):
            print("({0}, {1}) ({2}, {3}) ==> ({4}, {5}) ({6}, {7}) ==> {8}{9} ==> {10}".format(a[i][0], a[i][1], a[i+1][0], a[i+1][1], b[i][0], b[i][1], b[i+1][0], b[i+1][1], positiontoascii[b[i]], positiontoascii[b[i+1]], chr(int(positiontoascii[b[i]]+positiontoascii[b[i+1]], 2))))
            i += 2
        position = find_nearest(find_position(data))
        print(transform(position))


def find_nearest(data):
    result = []
    for i in data:
        #print(i)
        result.append(tuple(map(compare, i)))
        #print(result[-1])
    return result

def compare(number):
    correct_number = [-3, -1, 1, 3]
    temp = {}
    deviation = []
    if int(round(float(number))) not in correct_number:
        for i in correct_number:
            temp[abs(i-float(number))] = i
            deviation.append(abs(i-float(number)))
        return temp[min(deviation)]
    else:
        return int(round(float(number)))

def transform(data):
    bin_data = ""
    result = ""
    for i in data:
        if i not in positiontoascii:
            bin_data += "????"
        else:
            bin_data += positiontoascii[i]
    index = 0
    while index < len(bin_data):
        temp = bin_data[index:index+8]
        if "?" in temp:
            result += "_"
        else:
            result += chr(int(temp,2))
        index += 8
    return result

def find_position(data):
    result = []
    for i in data:
        a = i[i.index("(")+1:i.index(",")]
        b = i[i.index(",")+2:i.index(")")]
        result.append([a,b])
    return result

def ascii_to_position(data):
    index = 0
    result = []
    while index < len(data):
        result.append(asciitoposition[data[index:index+4]])
        index += 4
    return result

main()