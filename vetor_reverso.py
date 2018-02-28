import math
from time import time
from random import randint

def revert(list):
    revertList = []
    for n in list:
        revertList.append(list[-n])

    return revertList


def revertNative(list):
    reverListNative = reversed(list)
    return reverListNative






if __name__ == "__main__":
    size = 10000000
    list = []
    begin = time()
    end = time()
    diff = (end - begin) * 1000


    for i in range(size):
        list.append(randint(0, 10000000))


    print("Resultado : {}: Tempo : {}".format(revert(list)))
    print("Resultado : {}: Tempo : {}".format(revertNative(list)))


