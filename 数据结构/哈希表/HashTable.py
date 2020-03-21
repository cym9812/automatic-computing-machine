class HashTable:
    def __init__(self):
        self.__size = 5
        self.__slots = [None] * self.__size
        self.__data = [None] * self.__size
        self.__deleted = "\0"

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash,size):
        return (old_hash + 1) % size

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
            while self.__slots[next_slot] != None and self.__slots[next_slot] != self.__deleted \
                  and self.__slots[next_slot] != key:
                next_slot = self.rehash(next_slot,len(self.__slots))
                if next_slot == hash_value:
                    return
            if self.__slots[next_slot] == None or self.__slots[next_slot] == self.__deleted:
                self.__slots[next_slot] = key
                self.__data[next_slot] = data
            else:
                self.__data[next_slot] = data
                
    def delete(self, key):
        start_slot = self.hash_function(key, len(self.__slots))
        position = start_slot
        key_in_slot = self.__slots[position]

        while key_in_slot != None:
            if key_in_slot == key:
                self.__slots[position] = self.__deleted
                self.__data[position] = self.__deleted
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
        count = 0
        for value in self.__slots:
            if value != None and value != self.__deleted:
                count += 1
        return count

    def __contains__(self, key):
        return self.get(key) != None

    
    def __repr__(self):
        str_rep = "["
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
        return str_rep[:-2] + "]"
                





                
