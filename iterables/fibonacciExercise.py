class Fibonacci:
    def __init__(self):
        self.numbers = []
        self.index = -1

    def __iter__(self):
      return self

    def __next__(self):
        self.index += 1

        if self.index == 0 or self.index == 1:
            self.numbers.append(1)
            return 1
        else:
            self.numbers.append(self.numbers[self.index - 1] + self.numbers[self.index - 2])
            return self.numbers[self.index]

fib = Fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
