from math import sqrt, factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isprime(n):
            for i in range(2,1+int(sqrt(n))):
                if n %i == 0:
                    return False
            return True 
        primes, not_primes = 0, 1 # 1 is not prime
        for number in range(2, n+1):
            if isprime(number):
                primes += 1
            else:
                not_primes += 1
        print(primes, not_primes)
        return (factorial(primes)*factorial(not_primes))%1000000007


# print(Solution.numPrimeArrangements(Solution,100))



# Runtime: 38 ms, faster than 82.87% of Python3 online submissions for Prime Arrangements.
# Memory Usage: 13.8 MB, less than 66.53% of Python3 online submissions for Prime Arrangements.