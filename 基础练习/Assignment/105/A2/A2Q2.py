from Fibonacci import Fibonacci 

def main():
    user_input = input("Please enter a number between 1 and 50: ")
    while not(user_input.isdigit()) or int(user_input) < 1 or \
          int(user_input) > 50:
        user_input = input("Please enter a number between 1 and 50: ")
    n = int(user_input)
    print()
    print("The first",n,"term(s) of the Fibonacci sequence:")
    fib_obj = Fibonacci(n)
    for i in fib_obj:
        print(i, end=" ")
    print()
               
main()
