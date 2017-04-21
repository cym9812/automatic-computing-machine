def cost(time, number1, number2):
    adult = 100
    child = adult/2
    if time <= 5:
        price = number1 * adult + number2 * child
        return price
    else:
        price = number1 * adult / 2 + number2 * child / 2
        return price
while True:
    time = int(input("time: "))
    number1 = int(input("adults: "))
    number2 = int(input("children: "))
    total_cost = int(cost(time, number1, number2))
    print("total cost is ", total_cost, sep="")
