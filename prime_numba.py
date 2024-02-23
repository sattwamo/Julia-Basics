import time
from numpy import sqrt
from numba import jit 


@jit(nopython=True)
def prime_list():
    lower = 1 
    upper = 10**7 


    #print("Prime numbers between",lower,"and",upper,"are:")

    primes = []

    for num in range(lower,upper + 1):
    # prime numbers are greater than 1
        if num > 1:
            for i in range(2,int(sqrt(num))+1):
                if (num % i) == 0:
                    break
            else:
                #print(num)
                primes.append(num)
    #print(len(primes))
    #print(tot_time)


in_time = time.time()
prime_list()
tot_time = time.time() - in_time

print(tot_time)

## 9.442027807235718