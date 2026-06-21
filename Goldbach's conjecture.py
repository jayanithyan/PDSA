"""Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory. 
It states that every even number greater than 2 is the sum of two prime numbers.
For Example:
12=5+7
263 +23 or 7 + 19 or 13 +13
Write a function Goldbach(n) where n is a positive even number n > 2 ) that returns a list of tuples.
In each tuple (a, b) where ab, a and b should be prime numbers and the sum of a and b should be equal to n."""


def Goldbach(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for a in range(2, n // 2 + 1):
        b = n - a
        if is_prime(a) and is_prime(b):
            result.append((a, b))
    return result
n=int(input())
print(sorted(Goldbach(n)))