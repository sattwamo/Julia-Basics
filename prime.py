import time
from numpy import sqrt

lower = 1 
upper = 10**7


#print("Prime numbers between",lower,"and",upper,"are:")

primes = []

in_time = time.time()

for num in range(lower,upper + 1):
# prime numbers are greater than 1
    if num > 1:
        for i in range(2,int(sqrt(num))+1):
            if (num % i) == 0:
                break
        else:
            #print(num)
            primes.append(num)



tot_time = time.time() - in_time
print(len(primes))
print(tot_time)

## 664579
## 241.4270510673523