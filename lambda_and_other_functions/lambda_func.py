#-------------EASY EXAMPLE-------------

# sum = lambda x, y: x + y
# print(sum(5, 5))

#-------------NESTED EXAMPLE-------------

# canVote = lambda age: True if age >= 18 else False
# print(canVote(12))

#-------------LIST EXAMPLE-------------

# powerList = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
# for i in powerList:
#     print(i(2))

#-------------DICTIONARY EXAMPLE-------------

# attack = {'quick': (lambda: print('Quick Attack')), 'fast': (lambda: print('Fast Attack'))}
# listOfKeys = []

# for i in attack.keys():
#     listOfKeys.append(i)

# attackKey = random.choice(listOfKeys)
# attack[attackKey]()

#-------------FLIP LIST EXAMPLE-------------

# flipList = []

# for i in range(1, 101):
#     flipList.append(random.choice(['H', 'T']))

# print('Heads: ', flipList.count('H'))
# print('Tails: ', flipList.count('T'))