from math import sqrt
from functools import reduce

def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x/i != i:
                result.append(x/i)
        i += 1
    # Return the list of factors of x
    return result

def divsum(n): #returns the sum of proper divisors of n (includes 1, excludes n)
    sum = 0
    for i in factors(n):
        sum += i
    return sum-n

def isAmicable(n):
    k = divsum(n)
    return (divsum(k)==n)

amicable = [x for x in range(1,10000) if isAmicable(x)]

print(sum(amicable))