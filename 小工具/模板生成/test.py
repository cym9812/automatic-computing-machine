a = open("1.txt")
b = open("CapacitorCode.txt")
a = a.readlines()
b = b.readlines()
for i in range(len(a)):
    if a[i] != b[i]:
        print(i)
        print(a[i])
        print(b[i])
