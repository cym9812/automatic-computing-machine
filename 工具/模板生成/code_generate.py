import re

import pandas as pd


def capacitor_test():
    data = pd.read_csv("data.txt", delimiter="\t")
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
    capacitor.apply(write_capacitor_test, axis=1)


def write_capacitor_test(data):
    e = re.findall(r'\d+', data["E"])[0]
    tp1, tp2 = data["TPs"].split(",")
    with open("CapacitorCode.txt", "a") as output, open("model/CapacitorTestModel.txt") as model:
        temp = model.read()
        temp = temp.replace("(name)", data["RefDes"]) \
            .replace("(description)", data["Description"]) \
            .replace("(C)", data["C"]) \
            .replace("(E)", e) \
            .replace("(tp1)", tp1) \
            .replace("(tp2)", tp2)
        output.write(temp)
        output.write("\n")


def el_capacitor_test():
    data = pd.read_csv("data.txt", delimiter="\t")
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
    capacitor_el.apply(write_capacitor_el, axis=1)


def write_capacitor_el(data):
    e = re.findall(r'\d+', data["E"])[0]
    tp1, tp2 = data["TPs"].split(",")
    with open("ElCapacitorCode.txt", "a") as output, open("model/ElCapacitorTestModel.txt") as model:
        temp = model.read()
        temp = temp.replace("(name)", data["RefDes"]) \
            .replace("(description)", data["Description"]) \
            .replace("(C)", data["C"]) \
            .replace("(E)", e) \
            .replace("(tp1)", tp1) \
            .replace("(tp2)", tp2)
        output.write(temp)
        output.write("\n")


def resistor_test():
    data = pd.read_csv("data.txt", delimiter="\t")
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
    with open("ResistorCode.txt", "a") as output, open("model/ResistorTestModel.txt") as model:
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


def diode_test():
    data = pd.read_csv("data.txt", delimiter="\t")
    diode = data[(data["Partition"] == "Diode") | (data["Partition"] == "LED")].reset_index()
    diode = diode[["RefDes", "TPs", "Description"]]
    diode.apply(write_diode, axis=1)


def write_diode(data):
    tp1, tp2 = data["TPs"].split(",")
    with open("DiodeCode.txt", "a") as output, open("model/DiodeTestModel.txt") as model:
        temp = model.read()
        temp = temp.replace("(name)", data["RefDes"]) \
            .replace("(description)", data["Description"]) \
            .replace("(tp1)", tp1) \
            .replace("(tp2)", tp2)
        output.write(temp)
        output.write("\n")


def transistor_test():
    data = pd.read_csv("data.txt", delimiter="\t")
    transistor = data[(data["Partition"] == "Transistor") | (data["Partition"] == "Mosfet")].reset_index()
    transistor = transistor[["RefDes", "TPs", "Description"]]
    transistor.apply(write_transistor, axis=1)


def write_transistor(data):
    tps = data["TPs"].split(",")
    if len(tps) == 6:
        with open("TransistorMosfetCode.txt", "a") as output, open("model/TransistorTestModel.txt") as model:
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
        with open("TransistorMosfetCode.txt", "a") as output, open("model/TransistorTestModel.txt") as model:
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
    diode_test()
