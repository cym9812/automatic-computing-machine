#########################################
#   COMPSCI 105 S2 C, 2017              #
#   Assignment 1 Question 1             #
#                                       #
#   @author:     Yimeng Cai, ycai541    #
#   @version:    04/09/2017             #
#########################################

import json
from Item import Item

class Stock:
    # the constructor
    def __init__(self):
        self.__items = []

    # This function gets the number of items in stock.
    def get_size(self):
        return len(self.__items)

    # This function loads all the items on sale into the list.
    def load_items(self, filename):
        try:
            infile = open(filename, "r")
            stock_str = infile.read()
            infile.close()   
            stock_list = stock_str.split("\n")
            for item in stock_list:
                if item != "":
                    item_list = json.loads(item)
                    self.__items += [Item(item_list[0], item_list[1], item_list[2], item_list[3])]
        except IOError: 
            print("Error: File does not exist.")
    
    # This function saves all the items on sale into a file.
    def save_items(self, filename):     
        try:
            out_file = open(filename, 'w')
            for item in self.__items:
                item_list = [item.getCode(), item.getDescription(), item.getPrice(), item.getQuantity()]
                str_out = json.dumps(item_list)
                out_file.write(str_out + "\n")
            out_file.close()
        except IOError: 
            print("Error: File writing error.")

    #################################################################################################
    # The implementation of the above functions have already been given.                            #
    # Please DO NOT MODIFY the content of the ABOVE functions, as they are used by other functions. #
    # Please given the implementation of the following two functions to complete the program.       #
    #################################################################################################
    
    # This function finds an item on sale based on the item code.
    def find_item(self, code):
        for item in self.__items:
            if item.getCode() == code:
                return item
        return None
    
    # This function displays all the items on sale.
    def display_items(self):
        for item in self.__items:
            if item.getQuantity() > 0:
                print(item)
