'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from math import sqrt


def primes(n): #Naive way to calculate a prime list up to n. Everything that is a composite number is a multiple of some number. noprimes are all such multiples. 
    noprimes = set(j for i in range(2, n) for j in range(i*2, n, i))
    primes = [x for x in range(2, n) if x not in noprimes]
    return primes

def isPerm(n,m): #checks whether ints n and m are permutations of one another
    return sorted(str(n))==sorted(str(m))

big_primes = [i for i in primes(10000) if len(str(i))==4] #list of 4 digit primes.

'''
Let the two numbers big_primes[i] and big_primes[j] be the first two terms of the arithmetic progression. Generate the third term. If they are all three permutations of one another and prime, we are done.
'''
for i in range(len(big_primes)): 
    for j in range(i+1, len(big_primes)):
        k = big_primes[i]+2*(big_primes[j]-big_primes[i]) 
        if isPerm(big_primes[i], big_primes[j]) and isPerm(big_primes[i], k) and k in big_primes:
            print(str(big_primes[i])+' ' + str(big_primes[j])+' '+str(big_primes[i]+2*(big_primes[j]-big_primes[i])))
            break
            break
