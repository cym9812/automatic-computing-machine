while True:
    shuru = float(input("请输入十进制数字:"))
    erjizhi = []
    while shuru != 0:
        if shuru % 2 > 0:
            erjizhi.append(1)
        else:
            erjizhi.append(0)
        shuru = shuru // 2
    erjizhi.reverse()
    for a in erjizhi:
        print(a,end="")
    print()
    del erjizhi