def read_file(file_name):
    file_r = open(file_name, "r")
    content = file_r.readlines()
    print(content)



dic = {}
sum = 0
count = 0

while True:
    temp = input("数字: ")
    if temp == '':
        break
    frequency = int(input("频率: "))
    dic[int(temp)] = frequency
    sum += int(temp) * frequency
    count += frequency


avg = round(sum/count)
result = False
while True:
    Nob = 0
    Nbg = 0
    uob = 0
    ubg = 0
    for i in dic.keys():
        if i < avg:
            Nob += dic[i]
            uob += i * dic[i]
        else:
            Nbg += dic[i]
            ubg += i * dic[i]
    uob = round(uob/Nob)
    ubg = round(ubg/Nbg)
    result = round((uob+ubg)/2)
    print(result)
    if avg == result:
        break
    avg = result
print(result)