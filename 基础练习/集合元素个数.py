import itertools
origin = []
for i in itertools.product('012345678', repeat = 2):
    origin.append(i[0] + i[1])
result = []
count = 0
for i in origin:
    x = i[0]
    y = i[1]
    if int(x) + int(y) <= 9 and int(x) % 2 == int(y) % 2 and x + y not in result:
        result.append(x + y)
        count += 1
print(result)
print(count)
