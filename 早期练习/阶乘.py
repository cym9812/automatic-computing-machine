while True:
 a = float(input ("请输入想要进行阶乘运算的数字："))
 d = int(a)
 e = a-d
 if e>0:
    print("输入错误，请输入正整数")
    continue
 if a>100:
    print("数值过大请重新输入")
    continue
 if a == 0:
    print("结果是:1")
    continue
 if a == 1:
    print("结果是:1")
    continue
 if a<0:
    print("输入错误，请输入正整数")
 else:
         b=a-1
         c=a*b
         while b>1:
               b=b-1
               c=c*b
         print("结果是:%d"%(c))
