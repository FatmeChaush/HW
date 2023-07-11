def fib_number(n):
         n1 = 0
         n2=1
         sum = 0
         for itr in range(0, n):
            n1 = n2
            n2 = sum
            sum = n1 + n2
            print (sum, end="")

print(fib_number(10))