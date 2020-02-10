def integer_to_binary(value):
    result = ''
    if value:
        result = integer_to_binary(value // 2)
        return result + str(value % 2)
    else:
        return result
dec = int(input("请输入十进制数字"))
print(integer_to_binary(dec))
