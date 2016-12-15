arr = [8, 2, 5, 14, 3, 68, 7]


def arr_min(arr):
    if len(arr) == 0: return None
    m = arr[0]
    for e in arr:
        if e < m:
            m = e
    return m


print(arr_min(arr))


def av(arr):
    sum = 0
    for a in arr:
        sum +=a
    return (sum/len(arr))

print(av(arr))



