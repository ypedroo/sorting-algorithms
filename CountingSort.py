def find_min_max(items):
    min = items[0]
    max = items[0]

    for n in items:
        if n > max:
            max = n
        if n < min:
            min = n;

    return [min,max]

def get_position(items, n):
    result = None

    if items[0] == n:
        result = 0
    else:
        diff = n - items[0]
        result = diff

    return  result

def sort(items):
    result = find_min_max(items)
    min = result[0]
    max = result[1]

    index = []
    for n in range(min,max + 1):
        index.append(n)

    count = []
    for i in range(len(index)):
        count.append(0)
    for n in items:
        i = get_position(index, n)
        count[i] = count[i] + 1

    sum_count = []
    sum_count.append(count[0])
    for i in range(1, len(count)):
        sum_count.append(count[i] + sum_count[i - 1])

    result = []
    for i in range(len(items)):
        result.append(0)

    for n in items:
        position = get_position(index, n)
        j = sum_count[position] - 1
        result[j] = n

    return result


if __name__ == '__main__':
    sequencia = [10,7,12,4,9,13]
    print("seqInicial: " + str(sequencia))
    print("seqFinal: " + str(sort(sequencia)))















