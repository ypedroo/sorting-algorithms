import math

def create_bucket(base):
    buckets = []
    for i in range (base):
        buckets.append([])
        
    return buckets

def sort(items, base):
    tmp = -1
    j = 0
    
    m = int(math.log(items[0], base)) + 1
    
    while j < m:
    
        buckets = create_bucket(base)
        
        for number in items:
    
            tmp = number / math.pow(base, j)
            digit = int (tmp % base)
            buckets[digit].append(number)

        print(buckets)

        a = 0 
        for bucket in buckets:
            for i in bucket:
                items[a] = i
                a += 1

        
        j = j + 1

if __name__ == '__main__':
    list = [5, 10, 58, 23, 1, 2]
    
