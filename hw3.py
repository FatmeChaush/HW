def to_number(digits):
    num = 0
    for digit in digits:
        num = num * 10 + digit
    return num

print(to_number([1,2,3]))
print(to_number([9,9,9,9,9]))
print(to_number([1,2,3,0,2,3]))
print(to_number([21,2,33]))