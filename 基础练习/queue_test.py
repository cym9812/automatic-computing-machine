f1 = open("1.txt")
d1 = f1.readlines()
f2 = open("2.txt")
d2 = f2.readlines()

for i in range(len(d1)):
    print(d1[i] == d2[i])

