def to_digits(num):
    if num < 0:
        num = -num
    return[int(digit) for digit in str(num)]

print(to_digits(123))  
print(to_digits(99999)) 
print(to_digits(123023))   
