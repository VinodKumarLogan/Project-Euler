from math import sqrt
def sieve_primes(primes,n):
    for i in xrange(2,n):
        if primes[i]:
            for j in xrange(i*i,n,i):
                primes[j] = False
    return primes

def __main__():
    n=2000000
    primes = [True]*(n)
    primes[0] = False
    primes[1] = False
    primes = sieve_primes(primes,n)
    i=0
    for j in xrange(n):
        if primes[j]:
            i+=j
    print i

if __name__=='__main__':
    __main__()