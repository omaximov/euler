'''
Writing a large list of primes to a pickled file for later use.
'''
from sievefromgit import SieveOfAtkin
from math import sqrt, pow, ceil
import pickle




with open('primes_below_tenmillion', 'wb') as fp:
    pickle.dump(SieveOfAtkin(10000000).primes, fp)

print(SieveOfAtkin(100000).primes)