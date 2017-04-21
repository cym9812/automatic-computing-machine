print("-------欢迎使用通讯录-------")
print("--------1:查询联系人--------")
print("--------2:添加联系人--------")
print("--------3:删除联系人--------")
print("--------4:退出通讯录--------")
contact={"张三": "123456", "李四": "23456", "王五": "34567"}
while True:
    shuru=int(input("请输入指令代码:"))
    if shuru == 1:
        xingming = input("请输入姓名:")
        if xingming in contact:
            print("电话号码是:"+ contact[xingming])
        else:
            print("查无此人，请重新输入")
    if shuru == 2:
        xinmingzi = input("请输入姓名：")
        if xinmingzi in contact:
            print("联系人已存在，是否更新电话号码")
            fugaizhiling=int(input("如需覆盖请输入1，退回至主菜单请输入2: "))
            if fugaizhiling==1:
                dianhuahao = input("请输入电话号码:")
                contact[xinmingzi] = dianhuahao
                print("电话号码更新成功")
                continue
            if fugaizhiling==2:
                continue
        else:
            dianhuahao = input("请输入电话号码:")
            contact[xinmingzi] = dianhuahao
            print("储存成功")
    if shuru == 3:
        zhiling = int(input("输入1删除所有联系人，输入2删除指定联系人:"))
        if zhiling == 1:
            print("删除成功")
            contact.clear()
        if zhiling == 2:
            yaoshanchude = input("请输入要删除的联系人：")
            contact.pop(yaoshanchude)
        else:
            print("输入有误，跳回至主菜单")
            continue
    if shuru == 4:
        print("感谢使用本通讯录")
        break
