'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

#Technique: See that hexagonal numbers are given by triangular numbers for odd n. Thus, we need only check whether H_n is Pentagonal as well.
#According to Wikipedia, a quick way to check whether a number x is pentagonal is to check if ((sqrt(24*x + 1) + 1)/6 is a natural number. 

from math import sqrt

def is_pentagonal(n):
    p = (sqrt(24*n + 1) + 1)/6
    return p.is_integer()


n=143
while True:
    n+=1
    res = n*(2*n-1)
    if is_pentagonal(res):
        break
print(n*(2*n-1))