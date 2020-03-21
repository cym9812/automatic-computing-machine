from HashTable import HashTable

h_table = HashTable()
h_table[0] = "cat"
h_table[1] = "dog"
h_table[2] = "lion"
h_table[3] = "goat"
h_table[4] = "bird"
print(h_table,"size =",len(h_table))
del h_table[1]
del h_table[3]
del h_table[0]
print(h_table,"size =",len(h_table))
del h_table[2]
del h_table[4]
print(h_table,"size =",len(h_table))
del h_table[5]
print(h_table,"size =",len(h_table))
h_table[3] = "anteater"
h_table[71] = "cow"
print(h_table,"size =",len(h_table))


