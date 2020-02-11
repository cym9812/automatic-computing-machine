import os

def verify(file_name, method, compare):
    output = os.popen('certutil -hashfile ' + file_name + " " + method)
    result = output.read()
    result = result.split('\n')
    print("Expect: " + compare)
    print("Report: " + result[1] + "\n")
    print(result[1] == compare)

def check(file_name, method):
    os.system('certutil -hashfile ' + file_name + " " + method)

def main():
    method = ["MD5", "SHA1", "SHA256"]
    print("*" * 20)
    print("*     文件验证     *")
    print("*" * 20 + "\n")
    file_name = input("文件名: ")
    print()
    print("加密方式: 1.MD5   2.SHA1   3.SHA256\n")
    choose = method[(int(input("选择: ")) - 1)]
    print()
    compare = input("验证(可选): ")
    print()
    if compare == '':
        check(file_name, choose)
    else:
        verify(file_name, choose, compare)
    print()

while True:
    main()
    print()
