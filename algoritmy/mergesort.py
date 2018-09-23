def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    result.extend(left)
    result.extend(right)
    return result

def mergesort(m):
    left, right = [], []
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
    left = mergesort(left.copy())
    right = mergesort(right.copy())
    return merge(left.copy(),right.copy())

print(mergesort([1,3,2]))

