index = [1, 2]
result = 2
while index[-1] + index[-2] < 4000000:
    number = index[-1] + index[-2]
    index.append(number)
    if number % 2 == 0:
        result = result + number
print(result)
