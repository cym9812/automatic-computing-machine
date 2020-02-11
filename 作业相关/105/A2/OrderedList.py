######################################
#   COMPSCI 105 S2 C, 2017           #
#   Assignment 2 Question 1          #
#                                    #
#   @author:     Yimeng Cai, Ycai541 #
#   @version:    19/10/2017          #
######################################

from Node import Node
from LinkedListIterator import LinkedListIterator

class OrderedList:

    def __init__(self):
        self.__head = None
        self.__count = 0
    
    def is_empty(self):
        return self.__count == 0

    def size(self):
        return self.__count

    def add(self,item):
        new_node = Node(item)
        curr = self.__head
        prev = None
        self.add_recursive(new_node,curr,prev)

    def add_recursive(self,new_node,curr,prev):
        if curr == None:
            new_node.set_next(curr)
            if prev != None:
                prev.set_next(new_node)
            else:
                self.__head = new_node
        elif new_node.get_data() < curr.get_data():
            new_node.set_next(curr)
            if prev != None:
                prev.set_next(new_node)
            else:
                self.__head = new_node
        else:
            prev = curr
            self.add_recursive(new_node, curr.get_next(), prev)
        
    def search(self,item):
        curr = self.__head
        return self.search_recursive(item, curr)

    def search_recursive(self,item, curr):
        if curr != None:
            if curr.get_data() == item:
                return True
            elif curr.get_data() > item:
                return False
            else:
                curr = curr.get_next()
                return self.search_recursive(item, curr)
        else:
            return False

    def remove(self,item):
        curr = self.__head
        prev = None
        self.remove_recursive(item,curr,prev)
        
    def remove_recursive(self,item,curr,prev):
        if curr.get_data() == item:
            if prev == None:
                self.__head = curr.get_next()
            else:
                prev.set_next(curr.get_next())
        else:
            prev = curr
            curr = curr.get_next()
            self.remove_recursive(item, curr, prev)

    def __iter__(self):
        return LinkedListIterator(self.__head)

