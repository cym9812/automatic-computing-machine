######################################
#   COMPSCI 105 S2 C, 2017           #
#   Assignment 2 Question 1          #
#                                    #
#   @author:     Yimeng Cai, Ycai541 #
#   @version:    19/10/2017          #
######################################

from Fibonacci_Iterator import Fibonacci_Iterator

class Fibonacci:
    def __init__(self, number):
        count = 2
        if number == 1:
            self.__result = [1]
        elif number == 2:
            self.__result = [1, 1]
        else:
            self.__result = [1, 1]
            while count < number:
                self.__result += [self.__result[-1] + self.__result[-2]]
                count += 1


    def __iter__(self):
        return Fibonacci_Iterator(self.__result)
