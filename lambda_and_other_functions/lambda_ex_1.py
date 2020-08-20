import random

randomList = random.sample(range(1, 1001), 100)
multiplesOfNine = list(filter((lambda x: x % 9 == 0), randomList))

print(multiplesOfNine)