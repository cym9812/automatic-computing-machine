def hash2(key_word, table_size):
    total = 0
    for i in range(len(key_word)):
        total += (i + 1) * ord(key_word[i])
    return total % table_size

def main():
    print("table size is 13")
    for key_wd in ["cat","dog","abracadabra","abraabracad"]:
        print(key_wd, hash2(key_wd, 13))

main()

