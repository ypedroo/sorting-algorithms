import random
from time import time


def CreatList(n):
    alist = []
    for i in range(n, 0, -1):
        alist.append(random.randint(0, n))
    return alist


def Inplace_quick_sort(S, a, b):
    if a >= b: return
    pivot = S[b]
    left = a
    right = b - 1
    while left <= right:

        while left <= right and S[left] < pivot:
            left += 1

        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]

    Inplace_quick_sort(S, a, left - 1)
    Inplace_quick_sort(S, left + 1, b)


def performace(lenList):
    seqOri = CreatList(lenList)
    seq = list(seqOri)

    begin = time()
    Inplace_quick_sort(seq, 0, (len(seq) - 1))
    end = time()
    diff = (end - begin) * 1000
    print("inplace_quick_sort: " + str(diff))
    print("seq: " + str(seq))
    print(
        "****************************************************************************************************************************************************************************")

if __name__ == '__main__':
    performace(50)
    performace(100)
    performace(500)
    performace(1000)
    performace(10000)
