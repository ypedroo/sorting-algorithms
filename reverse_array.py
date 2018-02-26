import math
from time import time

def revertArray(list):
    reversedArray = []
    for n in list:
        reversedArray.append(list[-n])
    return reversedArray

def revertArray2(list):
    reversedArray2 = []
    for n in reversed(list):
        reversedArray2.append(n)

        
    return reversedArray2


      
 

if __name__ == "__main__":
   #list = lista = list(range(5000000))
   list = lista = [1,2,3,4,5]
   begin = time()
   end = time()
   diff = (end-begin) * 1000

   print("Resultado : {} : Tempo : {}".format(revertArray(list), diff))
   
   print("Resultado : {} : Tempo : {}".format(revertArray2(list), diff))
   