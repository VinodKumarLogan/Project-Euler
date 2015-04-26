from math import sqrt
def sieve_primes(primes,n):
    for i in xrange(2,n):
        if primes[i]:
            for j in xrange(i*i,n,i):
                primes[j] = False
    return primes

def __main__():
    n=11000000000
    sn=int(sqrt(n))
    primes = [True]*(sn)
    primes[0] = False
    primes[1] = False
    primes = sieve_primes(primes,sn)
    i=0
    for j in xrange(sn):
        if primes[j]:
            i+=1
        if i==10001:
            print j
            break

if __name__=='__main__':
    __main__()