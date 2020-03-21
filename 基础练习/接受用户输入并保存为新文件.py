name = input("请输入文件名:")
context = input("请输入文件内容，结尾输入#保存退出\n")
full_name = name + ".txt"
if "#" in context:
    (before, after) = context.split("#", 2)
    f = open(full_name, "a", )
    f.write(before)
    f.close()
    print("保存成功")
else:
    print("没有找到#，请重新输入")