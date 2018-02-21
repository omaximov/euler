'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
'''

def tripleGen(tot):
    trips = []
    c=0
    for c in range(1,tot):
        for b in range(1,c):
            for a in range(1,b):
                if a*a+b*b==c*c and a+b+c==tot:
                    trips.append([a,b,c])
    return len(trips)

p=0
max=0
for i in range(5,1001):
    length = tripleGen(i)
    if length>max:
        max = length
        p = i
print(max)
print(i)