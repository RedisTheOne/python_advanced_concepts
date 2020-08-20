from functools import reduce

#-------------MAP EXAMPLES-------------

oneToTen = range(1, 11)

def dblNum(num):
    return num * 2

print(list(map(dblNum, oneToTen)))

print(list(map((lambda x: x * 3), oneToTen)))

aList = list(map((lambda x, y: x + y), [1, 2, 3], [4, 5, 6]))
print(aList)

#-------------FILTER EXAMPLES-------------

print(list(filter((lambda x: x % 2 == 0), range(1, 11))))


#-------------REDUCE EXAMPLES-------------

print(reduce((lambda x, y: x + y), range(1, 6)))