'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

#brute force attempt

def n_to_n(limit):
    res = 0
    for i in range(1,limit+1):
        res+= i**i
    return res

print(n_to_n(1000))

#ran very quickly, i guess 1000^1001 is not bigger than python's limit for ints.