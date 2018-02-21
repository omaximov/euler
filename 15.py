'''
What is the sum of the digits of 2^1000?
'''

def digsum(n):
    xs = list(str(n)) #turns number into an array of characters
    soln = 0
    for i in xs:
        soln += int(i) #sum the array
    return soln

print(digsum(2**1000))