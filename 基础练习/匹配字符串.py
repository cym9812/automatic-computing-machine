def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    elif haystack == "":
        return -1
    else:
        match = True
        index = 0
        while index < len(haystack):
            for i in range(len(needle)):
                if haystack[index + i] != needle[i]:
                    inc = i
                    match = False
                    break
            if match:
                return index
            else:
                index += max(1,inc)
                match = True

        return -1

print(strStr("mississippi","issip"))


