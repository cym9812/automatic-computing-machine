number = 1000
factor1 = 3
factor2 = 5
count = 0
result = 0
while factor1 * count < 1000:
    result = result + factor1 * count
    count += 1
count = 0
while factor2 * count < 1000:
    result = result + factor2 * count
    count += 1
count = 0
while factor1 * factor2 * count < 1000:
    result = result - factor1 * factor2 * count
    count += 1
print(result)
