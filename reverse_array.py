import math
from time import time

def revertArray(list):
    reversedArray = []
    for n in list:
        reversedArray.append(list[-n])
    return reversedArray

if __name__ == "__main__":
   #list = list(range(5000000))
   list =  [1,2,3,4,5]
   begin = time()
   end = time()
   diff = (end-begin) * 1000

   #for i in range(size):
    #   list.append(randint(0, 10000000))
   print("Resultado : {} : Tempo : {}".format(list, diff))
   print("Resultado : {} : Tempo : {}".format(revertArray(list), diff))
   #print("Resultado : {} : Tempo : {}".format(list.reverse(), diff))
   #0lista = list(reversed(list)
   print("Resultado : {} : Tempo : {}".format(lista(reversed(list)), diff))

   