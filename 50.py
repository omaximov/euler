'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''
import pickle

with open ('primes_below_onemillion', 'rb') as fp:
    primes = pickle.load(fp)


max_l = 1
max_sum = 0
for i in range(len(primes)):
    curr_l = 1
    p_sum = i
    for j in range(i,len(primes)):
        if p_sum+j in primes:
            p_sum += j
            curr_l += 1
            if curr_l > max_l:
                max_l = curr_l
                max_sum = p_sum
                print(max_sum)
        else:
            break


