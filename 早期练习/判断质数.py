def p(num):
    try:
        for i in range(2, num):
            if num % i == 0:
                raise ValueError
    except ValueError:
        return p(num - 1)
    else:
        return num

print(p(10))
print(p(15))
print(p(200))
print(p(1900))
