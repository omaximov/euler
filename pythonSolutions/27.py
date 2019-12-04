def isPrime(n):
    for i in xrange(2,n):
        if n%1 ==0:
            return false
        else:
            return true

primes = filter(isPrime, range(-1000,1000))
