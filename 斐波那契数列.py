while True:
 def feibonaqi(n):
     if n == 1 or n == 2:
         return 1
     if n>2 :
         result=feibonaqi(n-1)+feibonaqi(n-2)
         return result
 number=int(input("请输入经过的月份:"))
 b=feibonaqi(number)
 print("共有%d对兔子"%(b))