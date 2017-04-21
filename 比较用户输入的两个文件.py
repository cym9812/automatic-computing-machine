while True:
    first_file = input("请输入需要比较的第一个文件名:\n")
    second_file = input("请输入需要比较的第二个文件名:\n")
    a = open(first_file, "r")
    liebiao1 = []
    b = open(second_file, "r")
    liebiao2 = []
    jishuqi = 0
    jishuqi2 = 0
    for each_line in a:
        liebiao1.append(each_line)
        jishuqi += 1
    for each_line in b:
        liebiao2.append(each_line)
    while jishuqi > 0:
        duibi1 = liebiao1[jishuqi2]
        duibi2 = liebiao2[jishuqi2]
        if duibi1 == duibi2:
            jishuqi2 += 1
            jishuqi -= 1
        else:
            jishuqi2 += 1
            print("第", jishuqi2, "行不同", sep = "")
            jishuqi -= 1
            continue