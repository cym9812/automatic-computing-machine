file = open("测试点.txt")
data = file.read()
data = data.split()
total = len(data)
count = 1
for i in data:
    with open("result_test.txt", "a") as output, open("finish_test.txt", "a") as finish:
        test_points = input(i + ": ")
        while len(test_points) % 3 != 0 or test_points == "":
            print("error")
            test_points = input(i + ": ")
        result = ""
        for j in range(0, len(test_points) - 2, 3):
            result = result.replace("\n", ",")
            result = result + "TP" + test_points[j:j + 3] + "\n"
        output.write(result)
        print(i + ": " + result)
        print("已完成{0}个/共{1}个 (进度{2}%)\n".format(count, total, round(count / total * 100)))
        count += 1
