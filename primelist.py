'''
Writing a large list of primes to a pickled file for later use.
'''

import pickle

def primes(n): 
    noprimes = set(j for i in range(2, n) for j in range(i*2, n, i))
    primes = [x for x in range(2, n) if x not in noprimes]
    return primes

with open('primes_below_onemillion', 'wb') as fp:
    pickle.dump(primes(1000000), fp)
