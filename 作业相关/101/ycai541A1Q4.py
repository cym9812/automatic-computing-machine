"""
Name: Yimeng Cai
username: ycai541
ID number: 455251836
Description:  the amount of each transaction is displayed, followed by the balance in parentheses (after the
transaction has been applied). The final two lines of output show the final balance and the overall sum of
the four transactions.
"""
import random
initial_balance = 768
transaction_min = 15
transaction_max = 501
current_balance = initial_balance
transaction_one = random.randrange(transaction_min, transaction_max) * random.randrange(-1, 2, 2)
transaction_two = random.randrange(transaction_min, transaction_max) * random.randrange(-1, 2, 2)
transaction_three = random.randrange(transaction_min, transaction_max) * random.randrange(-1, 2, 2)
transaction_four = random.randrange(transaction_min, transaction_max) * random.randrange(-1, 2, 2)
print("Initial bank balance: $", initial_balance, sep="")
print("=" * 26)
current_balance = current_balance + transaction_one
print("1: ", transaction_one, " (", current_balance, ")", sep="")
current_balance = current_balance + transaction_two
print("2: ", transaction_two, " (", current_balance, ")", sep="")
current_balance = current_balance + transaction_three
print("3: ", transaction_three, " (", current_balance, ")", sep="")
current_balance = current_balance + transaction_four
print("4: ", transaction_four, " (", current_balance, ")", sep="")
print("=" * 26)
print("Final bank balance: $", current_balance, sep="")
print("Sum of transactions: $", transaction_one + transaction_two + transaction_three + transaction_four, sep="")
print("=" * 26)
