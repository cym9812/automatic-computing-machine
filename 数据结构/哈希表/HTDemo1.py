from HashTable import HashTable

h_table = HashTable()
h_table[0] = "cat"
h_table[1] = "dog"
h_table[2] = "lion"
h_table[3] = "goat"
h_table[4] = "bird"
print(h_table)
del h_table[1]
del h_table[3]
print(h_table)
h_table[1] = "giraffe"
print(h_table)
h_table[6] = "zebra"
print(h_table)
