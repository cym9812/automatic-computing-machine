from Node import Node
from LinkedListIterator import LinkedListIterator

class UnorderedListTail:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def size(self):
        return self.__count

    def add_to_head(self,item):
        new_node = Node(item)
        new_node.set_next(self.__head)
        self.__head = new_node
        if self.__tail == None:
            self.__tail = new_node
        self.__count += 1

    def add_to_tail(self,item):
        if self.is_empty():
            self.add_to_head(item)
        else:
            new_node = Node(item)
            self.__tail.set_next(new_node)
            self.__tail = new_node
            self.__count += 1
        
    def search(self,item):
        curr = self.__head
        while curr != None:
            if curr.get_data() == item:
                return True
            else:
                curr = curr.get_next()
        return False

    def remove_from_head(self):
        self.__head = self.__head.get_next()
        if self.__head == None:
            self.__tail = None
        self.__count -= 1

    def remove_from_tail(self):
        if self.__head == self.__tail:
            self.remove_from_head()
        else:
            prev = self.__head
            while prev.get_next() != self.__tail:
                prev = prev.get_next()
            prev.set_next(None)
            self.__tail = prev
            self.__count -= 1

    def remove(self,item):
        if self.__head.get_data() == item:
            self.remove_from_head()
        elif self.__tail.get_data() == item:
            self.remove_from_tail()
        else:
            curr = self.__head.get_next()
            prev = self.__head
            while curr != self.__tail and curr.get_data() != item:
                prev = curr
                curr = curr.get_next()
            prev.set_next(curr.get_next())
            self.__count -= 1

    def __iter__(self):
        return LinkedListIterator(self.__head)        
