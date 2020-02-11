######################################
#   COMPSCI 105 S2 C, 2017           #
#   Assignment 1 Question 1          #
#                                    #
#   @author:     Yimeng Cai, ycai541 #
#   @version:    04/09/2017          #
######################################

from Item import Item

class Cart:
    # the constructor
    def __init__(self):
        self.__items = []
    
    # This function gets the number of items in the shopping cart.
    def get_size(self):
        return len(self.__items)

    #################################################################################################
    # The implementation of the above functions have already been given.                            #
    # Please DO NOT MODIFY the content of the ABOVE functions, as they are used by other functions. #
    # Please given the implementation of the following five functions to complete the program.      #
    #################################################################################################

    # This function adds an item into the shopping cart.
    def add_item(self, item):
        if int(item.getQuantity()) > 0:
            self.__items.append(item)
            item.setQuantity(int(item.getQuantity()) - 1)
            print("Item -", item.getDescription(), "is added to the shopping cart.")
        else:
            print("Sorry, item", item.getCode(), "is out of stock.")
            print("Please select a different item.")
    
    # This function finds an item on sale based on the item code.
    def find_item(self, code):
        for item in self.__items:
            if item.getCode() == code:
                return item
        return None

    # This function removes an item from the shopping cart.
    def delete_item(self, item):
        self.__items.remove(item)
        print("Item -", item.getDescription(), "is removed from the shopping cart.")
        item.setQuantity(int(item.getQuantity()) + 1)

    # This function clears everything in the shopping cart.
    def discard_all(self):
        while len(self.__items) > 0:
            item = self.__items.pop()
            item.setQuantity(int(item.getQuantity()) + 1)
        print("All items are removed from the shopping cart.")
    
    # This function prints out the items bought and calculates the total amount due.
    def check_out(self):
        amount = 0
        for item in self.__items:
            print("{0}/${1}".format(item.getDescription(), item.getPrice()))
            amount += float(item.getPrice())
        return amount
        ## IMPLEMENT THIS METHOD
