# sampStr = iter("Sample")

# print(next(sampStr))
# print(next(sampStr))
# print(next(sampStr))

class Alphabet:
   def __init__(self):
      self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      self.index = -1
   
   def __iter__(self):
      return self

   def __next__(self):
      if self.index >= len(self.letters) - 1:
         raise StopIteration
      self.index += 1
      return self.letters[self.index]

alpha = Alphabet()
#---WAY 1---

# print(next(alpha))
# print(next(alpha))

#---WAY 2---
for value in alpha:
   print(value)