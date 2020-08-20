def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generatePrimes(maxNumber):
    for num1 in range(2, maxNumber):
        print("Number: ", num1)
        if isPrime(num1):
            yield num1

prime = generatePrimes(50)
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))