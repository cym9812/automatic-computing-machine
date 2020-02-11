def Dec2Bin(dec):
    result = ''
    
    if dec:
        result = Dec2Bin(dec//2)
        return result + str(dec%2)
    else:
        return result
dec=int(input("请输入十进制数字"))
print(Dec2Bin(dec))
