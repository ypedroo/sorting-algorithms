#this algotithim is used to order a list in the inplace mode
def insertion_sort(A, comp):
    for k in range(1,len(A)):
        current = A[k]
        j = k

        while j > 0 and (comp (A[j - 1], current) < 0):
            A[j] = A[j - 1]
            j -= 1

        A[j] = current
        print(k, A)


def int_comparator(i,j):
    return j-i


if __name__ == '__main__':
    list = [5, 10, 58, 23, 1, 2]
    #insertion_sort(A)
    insertion_sort(list, int_comparator)




