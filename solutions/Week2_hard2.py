"""
Added by wendyjan 2/8/2016, from Project Euler and wikibooks.

The problem is #7 from Project Euler:
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10001st prime number?

Solution is from https://en.wikibooks.org/wiki/Some_Basic_and_Inefficient_Prime_Number_Generating_Algorithms
"""
from math import sqrt


def find_nth_prime(n):
    primes = [2, 3]
    potential_prime = 3
    while len(primes) < n:
        potential_prime += 2
        potential_prime_sqrt = sqrt(potential_prime)
        test = True
        for t in primes:
            if t > potential_prime_sqrt:
                break
            if potential_prime % t == 0:
                test = False
                break
        if test:
            primes.append(potential_prime)
    return primes[-1]


if __name__ == "__main__":
    print find_nth_prime(6)
    print find_nth_prime(10001)
