def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

filter_primes = lambda numbers: list(filter(lambda x: is_prime(x), numbers))

print(filter_primes([1,2,3,4,5,6,7,8,9,10]))