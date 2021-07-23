def prime(n, primeChecked):
  if (n == 1):
    return False
  elif (n == 2):
    return True
  else:
    for x in primeChecked:
      if (n % x == 0):
        return False
    return True

optimus = '{} is a prime number.'
optimusNot = '{} is a not a prime number.'
primeChecked = []

for n in range(1,300):

  if(prime(n, primeChecked)):
    primeChecked.append(n)
    print(optimus.format(n))
  else:
    print(optimusNot.format(n))
  
  print(primeChecked)
   
input()