######################################
#   COMPSCI 105 S2 C, 2017           #
#   Assignment 2 Question 1          #
#                                    #
#   @author:     Yimeng Cai, Ycai541 #
#   @version:    19/10/2017          #
######################################

class Fibonacci_Iterator:
    def __init__(self, result):
        self.__result = result
        self.__count = 0

    def __next__(self):
        if self.__count == len(self.__result):
            raise StopIteration
        else:
            self.__count += 1
            return self.__result[self.__count - 1]
