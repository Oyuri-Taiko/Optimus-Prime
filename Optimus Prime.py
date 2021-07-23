import random
import sys

def prime(n):
    
    if (n == 1):
        return False
    elif (n == 2) :
        return True
    else :
        for (x in range(2,n-1)):
            if (n % x == 0):
                return False
        return True
  
n = (random.randint(1,sys.maxsize))
print(n)

if (prime(n)):
    optimus = '{} is a prime number.'
    print(optimus.format(n))
else :
    optimusNot = '{} is a not a prime number.'
    print(optimusNot.format(n))

input()