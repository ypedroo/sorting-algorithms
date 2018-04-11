import random
from time import time


def CreatList(n):
    alist = []
    for i in range(n, 0, -1):
        alist.append(random.randint(0, n))
    return alist


def Inplace_InsertionSort(L):
    for i in range(1, len(L)):
        currentvalue = L[i]

        while i > 0 and L[i - 1] > currentvalue:
            L[i] = L[i - 1]
            i -= 1

        L[i] = currentvalue


def performace(lenList):
    seqOri = CreatList(lenList)
    seq1 = list(seqOri)

    begin = time()
    Inplace_InsertionSort(seq1)
    end = time()
    diff = (end - begin) * 1000
    print("Inplace_InsertionSort: " + str(diff))
    print("seq1: " + str(seq1))
    print("--------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    performace(50)
    performace(100)
    #performace(500)
    #performace(1000)
    #performace(10000)


