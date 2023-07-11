def is_number_balanced(n):
    if n < 10:
        return True

    digits = []
    for iter in range (0, n):
        digits.append(n % 10)
        n //= 10
        if(n == 0):
            break

    length = len(digits)
    mid = length // 2
    left_sum = sum(digits[:mid])
    right_sum = sum(digits[mid + length % 2:])

    return left_sum == right_sum
print(is_number_balanced(9))




