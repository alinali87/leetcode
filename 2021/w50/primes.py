def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    primes = [True if x == 2 or x % 2 == 1 else False for x in range(n)]
    primes[0] = False
    primes[1] = False
    i = 3
    while i * i < n:
        if not primes[i]:
            i += 1
            continue
        j = i * i
        while j < n:
            primes[j] = False
            j += i
        i += 1
    count = 0
    for el in primes:
        if el:
            count += 1
    return count


countPrimes(10)