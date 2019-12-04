def wordsum(s):
    sum = 0
    for i in s:
        sum += ord(i)-65
    return sum

file = open("p22_names.txt")
names1 = file.read().split(',')
names = [x.strip('\"') for x in names1]
names.sort()
sum = 0
for i in range(len(names)):
    sum += (i+1)*wordsum(names[i])
print(sum)