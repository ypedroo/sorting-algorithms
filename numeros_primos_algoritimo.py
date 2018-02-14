import math
from time import time


def prime(n):
   result = True

   for x in range(2, n):
       if n % x == 0:
           result = False
           break

   return result


def prime2(n):
       result = True

       k = (n // 2) + 1

       for x in range(2, k):
           if n % x == 0:
               result = False
               break

       return result


def prime3(n):
   result = True

   k = int(math.sqrt(n)) + 1

   for x in range(2,k):
       if n % x == 0:
           result = False
           break
   return result


def performance(function, n):
   begin = time()
   is_prime = function(n)
   end = time()
   diff = (end-begin) * 1000

   print("Resultado : {} : Tempo : {}".format(is_prime, diff))


if __name__ == "__main__":
   performance(prime, 100000)
   performance(prime2, 100000)
   performance(prime3, 100000)

