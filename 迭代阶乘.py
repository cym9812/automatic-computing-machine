a = int(input("请输入"))


def diedai(a):
    if a==1:
        return 1

    else:
        return a* diedai(a-1)
b = diedai(a)
print("%d的阶乘是%d"%(a,b))
