def prime(num):
    if num <= 1:
        return "Not prime"
    count = 2
    while count * count < num:
        if num % count == 0:
            return "Not Prime"
        count += 1
    return "prime"


# print(prime(2))