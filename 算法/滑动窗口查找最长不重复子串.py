a = "pwwkew"

def slide_window(s):
    n = len(s)
    ans = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    start = 0
    end = 0
    # 初始化两个指针
    dic = {}
    # 定义一个 map 数据结构存储 (k, v)，其中 key 值为字符，value 值为字符位置 +1
    for i in range(n):
        end = i
        if s[i] in dic:
            start = max(dic[s[i]], start)# 加 1 表示从字符位置后一个才开始不重复
        dic[s[i]] = end + 1
        ans = max(end - start + 1, ans)
    return ans

print(slide_window(a))

def slide_window2(arr):
    start = 0
    ans = 0
    dic = {}
    for i in range(len(arr)):
        end = i
        if arr[i] in dic:
            start = max(start, dic[arr[i]])
        dic[arr[i]] = end + 1
        ans = max(end - start + 1, ans)



