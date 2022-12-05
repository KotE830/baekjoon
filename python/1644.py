def sub_prime(n: int) -> int:
    def prime_numbers() -> list:
        primes = []
        is_prime = [True] * (n+1)

        for i in range(2, n+1):
            if is_prime[i]:
                primes.append(i)
                j = 2
                while i * j <= n:
                    is_prime[i*j] = False
                    j += 1
                
        return primes

    
    primes = prime_numbers()
    left, right, count, sums = 0, 0, 0, 0
    while right < len(primes):
        sums += primes[right]
        if sums < n:
            right += 1
        elif sums > n:
            sums -= primes[left]
            sums -= primes[right]
            left += 1
        else:
            count += 1
            sums -= primes[left]
            left += 1
            right += 1

    return count


n = int(input())
print(sub_prime(n))