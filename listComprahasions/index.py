import random

print([x * 2 for x in range(1, 11)])

print([x for x in range(1, 11) if x % 2 == 0])

print([x ** 2 for x in range(1, 50) if x % 8 == 0])

randomNumbers = random.sample(range(1, 1001), 50)
print([x for x in [y for y in randomNumbers if y % 9 == 0]])