import math

import pandas as pd


def count_frequency(classification, data):
    temp = []
    for i in data:
        if i not in common_words:
            temp.append(i)
    count = len(temp)
    for i in temp:
        if i not in classification.keys():
            classification[i] = 1
        else:
            classification[i] += 1
    return count


def clean_common_words(data):
    cleaned = []
    for i in data:
        if i in common_words:
            pass
        else:
            cleaned.append(i)
    return cleaned


def probability(dic, word, dic_count, total_len):
    if word in dic.keys():
        return (dic[word] + 1) / (dic_count + total_len)
    return 1 / (dic_count + total_len)


def find_max(pa, pb, pe, pv):
    if pa > pb and pa > pe and pa > pv:
        result = "A"
    elif pb > pa and pb > pe and pb > pv:
        result = "B"
    elif pe > pa and pe > pb and pe > pv:
        result = "E"
    elif pv > pa and pv > pb and pv > pe:
        result = "V"
    else:
        result = "?"
    return result


def main():
    train_data = pd.read_csv("trg.csv")
    class_size = train_data.groupby("class").size()
    ca = class_size[0] / train_data.shape[0]
    cb = class_size[1] / train_data.shape[0]
    ce = class_size[2] / train_data.shape[0]
    cv = class_size[3] / train_data.shape[0]
    # print(ca, cb, ce, cv)
    a = {}
    b = {}
    e = {}
    v = {}
    a_count = 0
    b_count = 0
    e_count = 0
    v_count = 0
    output = []
    for each in train_data.values:
        temp = each[2].split()
        temp = [i.lower() for i in temp]
        if each[1] == 'A':
            a_count += count_frequency(a, temp)
        elif each[1] == 'B':
            b_count += count_frequency(b, temp)
        elif each[1] == 'E':
            e_count += count_frequency(e, temp)
        elif each[1] == 'V':
            v_count += count_frequency(v, temp)
    total = set(list(a.keys()) + list(b.keys()) + list(e.keys()) + list(v.keys()))
    test_data = pd.read_csv("tst.csv")

    for each in test_data.values:
        temp = each[1].split()
        temp = [i.lower() for i in temp]
        pa = 1
        pb = 1
        pe = 1
        pv = 1
        total_len = len(set(list(total) + clean_common_words(temp)))
        for word in temp:
            if word in common_words:
                continue
            pa += math.log(probability(a, word, a_count, total_len))
            pb += math.log(probability(b, word, b_count, total_len))
            pe += math.log(probability(e, word, e_count, total_len))
            pv += math.log(probability(v, word, v_count, total_len))
        pa += math.log(ca)
        pb += math.log(cb)
        pe += math.log(ce)
        pv += math.log(cv)
        output.append(find_max(pa, pb, pe, pv))

    out = open("result.csv", "w")
    out.write("id,class\n")
    for j in range(0, len(output)):
        out.write(str(j + 1) + "," + output[j] + "\n")
    out.close()

    print("A:", output.count("A"))
    print("B:", output.count("B"))
    print("E:", output.count("E"))
    print("V:", output.count("V"))

    print(len(a.keys()))
    print(len(b.keys()))
    print(len(e.keys()))
    print(len(v.keys()))


if __name__ == '__main__':
    file = open("5000words.txt")
    text = file.read()
    file.close()
    common_words = text.split()
    common_words = common_words[:100]
    main()
