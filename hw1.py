def sum_of_digits(num):
    result = 0

    for iter in range(0, 3):
        result = result + num % 10
        num = num // 10 
    return result
print(sum_of_digits(235))
