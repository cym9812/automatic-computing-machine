import re
import time

import pandas as pd


def capacitor_test(data):
    capacitor = data[(data["Partition"] == "Capacitor") & (data["Parallel Capacitor"].isnull())]
    capacitor = capacitor.reset_index()
    test_config = []
    description = capacitor["Description"]
    for i in description:
        temp = i.replace(" ", "_").split("_")
        v_position = -1
        for j in range(len(temp)):
            if temp[j][-1] == "V":
                v_position = j
                break
        test_config.append([temp[v_position - 2], temp[v_position - 1], temp[v_position]])
    test_config = pd.DataFrame(data=test_config, columns=["C", "E", "V"])
    capacitor = pd.concat([capacitor[["RefDes", "TPs", "Description"]], test_config], axis=1)
    with open("CapacitorCode.txt", "w") as output:
        output.write("    'Total {0} components.\n\n".format(len(capacitor)))
    capacitor.apply(write_capacitor_test, axis=1)


def write_capacitor_test(data):
    e = re.findall(r'\d+', data["E"])[0]
    tp1, tp2 = data["TPs"].split(",")
    global private_signal_FDCIO162
    global private_signal_FDCIO164
    if private_signal_FDCIO162:
        file_name = "CapacitorCode_FDCIO162.txt"
    elif private_signal_FDCIO164:
        file_name = "CapacitorCode_FDCIO164.txt"
    else:
        file_name = "CapacitorCode.txt"
    with open(file_name, "a") as output, open("model/CapacitorTestModel.txt") as model:
        temp = model.read()
        temp = temp.replace("(name)", data["RefDes"]) \
            .replace("(description)", data["Description"]) \
            .replace("(C)", data["C"]) \
            .replace("(E)", e) \
            .replace("(tp1)", tp1) \
            .replace("(tp2)", tp2)
        output.write(temp)
        output.write("\n")


def el_capacitor_test(data):
    capacitor_el = data[(data["Partition"] == "Capacitor_EL") & (data["Parallel Capacitor"].isnull())]
    capacitor_el = capacitor_el.reset_index()
    test_config = []
    description = capacitor_el["Description"]
    for i in description:
        temp = i.replace(" ", "_").split("_")
        v_position = -1
        for j in range(len(temp)):
            if temp[j][-1] == "V":
                v_position = j
                break
        test_config.append([temp[v_position - 2], temp[v_position - 1], temp[v_position]])
    test_config = pd.DataFrame(data=test_config, columns=["C", "E", "V"])
    capacitor_el = pd.concat([capacitor_el[["RefDes", "TPs", "Description"]], test_config], axis=1)
    with open("ElCapacitorCode.txt", "w") as output:
        output.write("    'Total {0} components.\n\n".format(len(capacitor_el)))
    capacitor_el.apply(write_capacitor_el, axis=1)


def write_capacitor_el(data):
    e = re.findall(r'\d+', data["E"])[0]
    tp1, tp2 = data["TPs"].split(",")
    global private_signal_FDCIO162
    global private_signal_FDCIO164
    if private_signal_FDCIO162:
        file_name = "ElCapacitorTestCode_FDCIO162.txt"
    elif private_signal_FDCIO164:
        file_name = "ElCapacitorTestCode_FDCIO164.txt"
    else:
        file_name = "ElCapacitorTestCode.txt"
    with open(file_name, "a") as output, open("model/ElCapacitorTestModel.txt") as model:
        temp = model.read()
        temp = temp.replace("(name)", data["RefDes"]) \
            .replace("(description)", data["Description"]) \
            .replace("(C)", data["C"]) \
            .replace("(E)", e) \
            .replace("(tp1)", tp1) \
            .replace("(tp2)", tp2)
        output.write(temp)
        output.write("\n")


def resistor_test(data):
    resistor = data[data["Partition"] == "Resistor"].reset_index()
    test_config = []
    description = resistor["Description"]
    for i in description:
        temp = i.replace(" ", "_").split("_")
        e_position = -1
        for j in range(len(temp)):
            if temp[j][-1] == "%":
                e_position = j
                break
        if temp[e_position - 1] == "OHM":
            test_config.append([temp[e_position - 2], temp[e_position]])
        else:
            test_config.append([temp[e_position - 1], temp[e_position]])
    test_config = pd.DataFrame(data=test_config, columns=["R", "E"])
    resistor = pd.concat([resistor[["RefDes", "TPs", "Description"]], test_config], axis=1)
    with open("ResistorCode.txt", "w") as output:
        output.write("    'Total {0} components.\n\n".format(len(resistor)))
    resistor.apply(write_resistor, axis=1)


def write_resistor(data):
    e = re.findall(r'\d+', data["E"])[0]
    r = data["R"].replace("R", "").upper()
    temp = r
    if "M" in temp:
        if "." in temp:
            temp = temp.replace("M", "")
        else:
            temp = temp.replace("M", ".")
        temp = float(temp) * 1000000
    elif "K" in temp:
        if "." in temp:
            temp = temp.replace("K", "")
        else:
            temp = temp.replace("K", ".")
        temp = float(temp) * 1000
    else:
        temp = float(temp)
    if temp <= 100:
        v = "50"
    else:
        v = "250"
    tp1, tp2 = data["TPs"].split(",")
    global private_signal_FDCIO162
    global private_signal_FDCIO164
    if private_signal_FDCIO162:
        file_name = "ResistorTestCode_FDCIO162.txt"
    elif private_signal_FDCIO164:
        file_name = "ResistorTestCode_FDCIO164.txt"
    else:
        file_name = "ResistorTestCode.txt"
    with open(file_name, "a") as output, open("model/ResistorTestModel.txt") as model:
        temp = model.read()
        temp = temp.replace("(name)", data["RefDes"]) \
            .replace("(description)", data["Description"]) \
            .replace("(size)", data["R"]) \
            .replace("(voltage)", v) \
            .replace("(size_no_R)", r) \
            .replace("(e)", e) \
            .replace("(tp1)", tp1) \
            .replace("(tp2)", tp2)
        output.write(temp)
        output.write("\n")


def diode_test(data):
    diode = data[(data["Partition"] == "Diode") | (data["Partition"] == "LED")].reset_index()
    diode = diode[["RefDes", "TPs", "Description"]]
    with open("DiodeCode.txt", "w") as output:
        output.write("    'Total {0} components.\n\n".format(len(diode)))
    diode.apply(write_diode, axis=1)


def write_diode(data):
    tp1, tp2 = data["TPs"].split(",")
    global private_signal_FDCIO162
    global private_signal_FDCIO164
    if private_signal_FDCIO162:
        file_name = "DiodeTestCode_FDCIO162.txt"
    elif private_signal_FDCIO164:
        file_name = "DiodeTestCode_FDCIO164.txt"
    else:
        file_name = "DiodeTestCode.txt"
    with open(file_name, "a") as output, open("model/DiodeTestModel.txt") as model:
        temp = model.read()
        temp = temp.replace("(name)", data["RefDes"]) \
            .replace("(description)", data["Description"]) \
            .replace("(tp1)", tp1) \
            .replace("(tp2)", tp2)
        output.write(temp)
        output.write("\n")


def transistor_test(data):
    transistor = data[(data["Partition"] == "Transistor") | (data["Partition"] == "Mosfet")].reset_index()
    transistor = transistor[["RefDes", "TPs", "Description"]]
    with open("TransistorMosfetCode.txt", "w") as output:
        output.write("    'Total {0} components.\n\n".format(len(transistor)))
    transistor.apply(write_transistor, axis=1)


def write_transistor(data):
    tps = data["TPs"].split(",")
    global private_signal_FDCIO162
    global private_signal_FDCIO164
    if private_signal_FDCIO162:
        file_name = "TransistorTestCode_FDCIO162.txt"
    elif private_signal_FDCIO164:
        file_name = "TransistorTestCode_FDCIO164.txt"
    else:
        file_name = "TransistorTestCode.txt"
    if len(tps) == 6:
        with open(file_name, "a") as output, open("model/TransistorTestModel.txt") as model:
            temp = model.read()
            temp = temp.replace("(name)", data["RefDes"] + "/1") \
                .replace("(description)", data["Description"]) \
                .replace("(tp1)", tps[0]) \
                .replace("(tp2)", tps[1]) \
                .replace("(tp3)", tps[2])
            output.write(temp)
            output.write("\n")
            temp = model.read()
            temp = temp.replace("(name)", data["RefDes"] + "/2") \
                .replace("(description)", data["Description"]) \
                .replace("(tp1)", tps[3]) \
                .replace("(tp2)", tps[4]) \
                .replace("(tp2)", tps[5])
            output.write(temp)
            output.write("\n")

    elif len(tps) == 3:
        with open(file_name, "a") as output, open("model/TransistorTestModel.txt") as model:
            temp = model.read()
            temp = temp.replace("(name)", data["RefDes"]) \
                .replace("(description)", data["Description"]) \
                .replace("(tp1)", tps[0]) \
                .replace("(tp2)", tps[1]) \
                .replace("(tp3)", tps[2])
            output.write(temp)
            output.write("\n")
    else:
        print("error")


if __name__ == '__main__':
    # 读取文件
    df = pd.read_csv("data.txt", delimiter="\t")
    private_signal_FDCIO162 = False
    private_signal_FDCIO164 = False

    # 共有部分
    print("开始处理公有部分")
    time_start = time.time()

    public = df[(df["FDCIO162"].isnull()) & (df["FDCIO164"].isnull())]

    capacitor_test(public)
    el_capacitor_test(public)
    resistor_test(public)
    diode_test(public)
    transistor_test(public)

    time_end = time.time()
    print("公有部分处理完成")
    print('耗时：', time_end - time_start, "\n")

    # 私有部分
    print("开始处理私有部分")

    private_FDCIO162 = df[-(df["FDCIO164"].isnull())]
    private_FDCIO164 = df[-(df["FDCIO162"].isnull())]

    # FDCIO162
    time_start = time.time()

    private_signal_FDCIO162 = True
    capacitor_test(private_FDCIO162)
    el_capacitor_test(private_FDCIO162)
    resistor_test(private_FDCIO162)
    diode_test(private_FDCIO162)
    transistor_test(private_FDCIO162)
    private_signal_FDCIO162 = False

    time_end = time.time()
    print("FDCIO162处理完成")
    print('耗时：', time_end - time_start, "\n")

    # FDCIO164
    time_start = time.time()

    private_signal_FDCIO164 = True
    capacitor_test(private_FDCIO164)
    el_capacitor_test(private_FDCIO164)
    resistor_test(private_FDCIO164)
    diode_test(private_FDCIO164)
    transistor_test(private_FDCIO164)

    time_end = time.time()
    print("FDCIO164处理完成")
    print('耗时：', time_end - time_start, "\n")
    # 不包含并联电容
    print("capacitor, el_capacitor, resistor, diode, transistor代码生成完成")
