from itertools import permutations
fanwei = list(permutations("123456789"))
create_var = locals()
m = 0
index1 = []
index2 = []
while fanwei:
    temp = fanwei.pop()
    n = 1
    for value in temp:
        create_var['x'+str(n)] = int(value)
        n += 1
    if x1 + x2 / x3 + (x4 * x5 * x6) / (x7 * x8 * x9) == 10:
        d = str(x1) + str(x2) + str(x3)
        e = x7 * x8 * x9
        if d in index1 and e in index2:
            continue
        else:
            print(x1, x2, x3, x4, x5, x6, x7, x8, x9)
            index1.append(d)
            index2.append(e)
            m += 1
    else:
        continue
print("结果数量:", m)
