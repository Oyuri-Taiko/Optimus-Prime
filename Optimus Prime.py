def prime(n):
    if (n == 1):
       return False
    elif (n == 2):
       return True
    else:
        for x in range(2,n-1):
            if (n % x == 0):
                return False
        return True

optimus = '{} is a prime number.'
optimusNot = '{} is a not a prime number.'

for n in range(1,300):
  if (prime(n)):
    print(optimus.format(n))
  else:
    print(optimusNot.format(n))
    
input()