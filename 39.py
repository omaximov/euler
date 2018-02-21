'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
'''



'''
Intuition for solution: integers a,b,c such that a^2+b^2=c^2. Moreover, we need a+b+c=P, for fixed P (which we iterate).
substituting for c, see that we need only iterate over a, and find b such that 

b=p(p-2a)/(2(p-a)).

If this expression is an integer, then it must be that c is an integer. 
Moreover, we can reduce the range for which we iterate over a by observing that a+b>c, a+c>b, and b+c>a. Therefore, a is bounded by p/(2+sqrt(2)).

'''
L=1000
t_max = 0
p_max = 0


for p in range(L//4*2, L+1, 2):
    t = 0
    for a in range(2, int(p/3.4142) + 1):
        if  p*(p - 2*a) % (2*(p - a)) == 0: 
            t += 1
            if t >= t_max: 
                t_max = t
                p_max = p

print("Greatest perimiter is "+str(p_max)+" with "+str(t_max)+ " triangles.")