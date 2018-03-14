def merge(S1, S2, S):
    """merge two sorted python lists S1 and S2 into properly sized list S """

    print("merging" + str(S1) + " and " + str(S2))
    i = j = 0
    while i +j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i] #copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j] # copy jth element of S2 as next item of S
            j += 1

    print("Merged" + str(S) + "\n")

def sort(S):
    n = len(S)


    if n < 2:
        return

    #divide
    mid = int(n/2)
    S1 = S[0:mid] #copy of the first half
    S2 = S[mid:n] #copy of the second half
    print("S1: " + str(S1))
    print("S2: " + str(S2))

    #conquer with (recursion)
    sort(S1) #sort copy of first half
    sort(S2) #sort copy of second half

    #merge results
    merge(S1, S2, S)


if __name__ == "__main__":
    list = [1, 25, 54, 10, 58, 4841, 112, 45487]
    merge(list)



