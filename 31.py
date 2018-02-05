clist = [1, 2, 5, 10, 20, 50, 100, 200]


def numways(coinlist, target):
    ways = [1]+[0]*target
    for coin in coinlist:
        for i in range(coin,target+1):
            ways[i]+=ways[i-coin]
    return ways[target]

print(numways(clist, 200))
