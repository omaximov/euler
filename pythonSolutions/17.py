'''
How many letters are used to spell out all the numbers between 1 and 1000 (inclusive). 
We are not counting spaces or hyphens, but we ARE counting "and" as in "one hundred and twelve"
'''

nums = {
    0 : '', 
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'hundred',
    1000 : 'thousand' 
}

def numToWord(n): #this recursive solution is perhaps best implemented in Haskell-- unless I can avoid (easily) avoid recursion
    if n == 1000:
        return 'onethousand'
    if n<21:
        return nums[n]
    s = str(n)
    if len(s)==2:
        return nums[10*(int(s[0]))]+nums[int(s[1])]
    if len(s) ==3:
        return nums[int(s[0])]+nums[100]+'and'+numToWord(int(s[1:])) 
    

result = 0
for i in range(1,1001):
    result += len(numToWord(i))
print(result)
    