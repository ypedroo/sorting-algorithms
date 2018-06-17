def find_index(array, k):
    result = 0

    for index in range(len(array)):
        n = array[index]

        if n <= k:
            result = index
        else:
            break 

    return result

def iterate(array, k, left, right):
    i = array[left]
    j = array[right]

    if (i  + j) == k:
        return left, right
    elif (i + j) < k:
        left, right = iterate(array, k, left + 1, right)
    elif (i + j) > k:
        left, right = iterate(array, k, left, right - 1)

    return left, right

def find_sum(array, k):
    index = find_index(array, k)

    left = 0
    right = index

    if left < right:
        left, right = iterate(array, k , left, right)
        
    return left, right

if __name__ == "__main__":
    array = [1, 2, 3, 4, 6, 7, 8]
    k = 16

    left, right = find_sum(array, k)

    print(array[left], array[right])