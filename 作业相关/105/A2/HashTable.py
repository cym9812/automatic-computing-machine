######################################
#   COMPSCI 105 S2 C, 2017           #
#   Assignment 2 Question 1          #
#                                    #
#   @author:     Yimeng Cai, Ycai541 #
#   @version:    19/10/2017          #
######################################
class HashTable:
    def __init__(self):
        self.__size = 7
        self.__slots = [None] * self.__size
        self.__data = [None] * self.__size
        self.__deleted = "\0"
        self.__count = 0

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash,size):
        return (old_hash + (size - (old_hash % (size - 1)+1))) % size

    def load_factor(self, count):
        return count / self.__size

    def largest_prime_number(self, current_size):
        result = current_size * 2 - 1
        try:
            for i in range(2, result):
                if result % i == 0:
                    raise ValueError
        except ValueError:
            return self.largest_prime_number(result - 1)
        else:
            return result

    def resize(self):
        slot_temp = self.__slots[:]
        data_temp = self.__data[:]
        self.__size = self.largest_prime_number(self.__size)
        self.__slots = [None] * self.__size
        self.__data = [None] * self.__size
        for i in slot_temp:
            if i != None and i != self.__deleted:
                self.put(i, data_temp[slot_temp.index(i)])
                self.__count -= 1


    def get(self, key):
        start_slot = self.hash_function(key,len(self.__slots))
        position = start_slot

        while self.__slots[position] != None:
            if self.__slots[position] == key:
                return self.__data[position]
            else:
                position = self.rehash(position, len(self.__slots))
                if position == start_slot:
                    return None
        return None

    def put(self,key,data):
        hash_value = self.hash_function(key,len(self.__slots))
        if self.__slots[hash_value] == None or self.__slots[hash_value] == self.__deleted:
            self.__slots[hash_value] = key
            self.__data[hash_value] = data
        elif self.__slots[hash_value] == key:
            self.__data[hash_value] = data
        else:
            next_slot = self.rehash(hash_value, len(self.__slots))
            while self.__slots[next_slot] != None\
                  and self.__slots[next_slot] != self.__deleted \
                  and self.__slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.__slots))
                if next_slot == hash_value:
                    return
            if self.__slots[next_slot] == None or self.__slots[next_slot] == self.__deleted:
                self.__slots[next_slot] = key
                self.__data[next_slot] = data
            else:
                self.__data[next_slot] = data
        self.__count += 1
        if self.load_factor(self.__count) > 0.75:
            self.resize()

    def delete(self, key):
        start_slot = self.hash_function(key, len(self.__slots))
        position = start_slot
        key_in_slot = self.__slots[position]

        while key_in_slot != None:
            if key_in_slot == key:
                self.__slots[position] = self.__deleted
                self.__data[position] = self.__deleted
                self.__count -= 1
                return None	
            else:
                position = self.rehash(position, len(self.__slots))
                key_in_slot = self.__slots[position]
                if position == start_slot:
                    return None
        return None

    def __delitem__(self, key):
        return self.delete(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __getitem__(self,key):
        return self.get(key)

    def __len__(self):
        return self.__count

    def __contains__(self, key):
        return self.get(key) != None

    
    def __repr__(self):
        str_rep = "{"
        for i in range(len(self.__slots)):
            key = self.__slots[i]
            data = self.__data[i]
            info = ""
            if key == None or key == self.__deleted:
                info = ""
            else:
                if data == None:
                    info = str(key) + ":None"
                else:
                    info = str(key) + ":" + str(data)
            str_rep += info + ", "
        return str_rep[:-2] + "}"
                





                
