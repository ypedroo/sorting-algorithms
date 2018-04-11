#Implementation of MergeSort recurssive and interactive
#with Timers for academic propurses
import random
from time import time


def createList(n):
    alist = []
    for i in range(n, 0, -1):
        alist.append(random.randint(0, n))
    return alist


def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)


def merge_2(seq):
    listOfLists = []
    for i in range(len(seq)):
        temp = [seq[i]]
        listOfLists.append(temp)

    while (len(listOfLists) != 1):
        j = 0

        while (j < len(listOfLists) - 1):
            tempList = merge(listOfLists[j], listOfLists[j + 1])
            listOfLists[j] = tempList
            del listOfLists[j + 1]
            j = j + 1

def merge(a, b):
    newList = []
    a1, a2 = 0, 0

    while ((a1 < len(a)) and (a2 < len(b))):
        if (a[a1] > b[a2]):
            newList.append(b[a2])
            a2 = a2 + 1
        elif (a[a1] < b[a2]):
            newList.append(a[a1])
            a1 = a1 + 1
        elif (a[a1] == b[a2]):
            newList.append(a[a1])
            newList.append(b[a2])
            a1, a2 = a1 + 1, a2 + 1
    if (a1 < len(a)):
        for f in range(a1, len(a)):
            newList.append(a[f])
    elif (a2 < len(b)):
        for k in range(a2, len(b)):
            newList.append(b[k])
    return newList



def performace(lenList):
    seqOri = createList(lenList)
    seq1 = list(seqOri)
    seq2 = list(seqOri)

    begin = time()
    mergeSort(seq1)
    end = time()
    diff = (end - begin) * 1000
    print("Recursive: " + str(diff))
    print("seq1: " + str(seq1))
    print("")

    begin = time()
    merge_2(seq2)
    end = time()
    diff = (end - begin) * 1000
    print("interative: " + str(diff))
    print("seq2: " + str(seq2))
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



if __name__ == '__main__':
    performace(10)
    #performace(500)
    #performace(1000)
    #performace(10000)














