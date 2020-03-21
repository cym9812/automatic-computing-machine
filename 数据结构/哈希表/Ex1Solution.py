def hash1(key_word, table_size):
    total = 0
    for char in key_word:
        total += ord(char)
    return total % table_size

def main():
    print("table size is 13")
    for key_wd in ["cat","dog","abracadabra","abraabracad"]:
        print(key_wd, hash1(key_wd, 13))

main()
