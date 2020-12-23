def countPrimes( n):
    #sieve of erastosthesnes
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    count=0
    print(prime)
    for i in range(2, n + 1):
        if prime[i]:
            count+=1
    return count
    #return prime.count(True)
print(countPrimes(3))