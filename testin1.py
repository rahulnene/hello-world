import math

abundants = []

def divisorGenerator(n):
    large_divisors = []
    yield 1
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def abundant(k):
    sum = 0
    for i in list(divisorGenerator(k)):
        sum += i
    if sum > k: return 1
    else: return 0

def generateAbundants:
    for n in range(24,28123):
        if abundant(n):
            abundants.append(n)

def main:
    generateAbundants()

main()