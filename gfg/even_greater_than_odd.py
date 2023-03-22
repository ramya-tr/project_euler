"""
Given an array A of n elements, sort the array according to the following relations :
A[i] >= A[i-1]                   , if i is even.
A[i] <= A[i-1]                   , if i is odd.
Print the resultant array.
"""
def even_greater_than_odd1():
    a = [1, 2, 2, 1, 1, 2, 3, 4, 5, 6, 6, 5, 4]

    i, j = 0, 0
    b = [a[0]]
    del a[0]

    while i < len(a):
        if j % 2 == 0:
            if a[i] >= b[j]:
                b.append(a[i])
                del a[i]
                j += 1
                i = 0
            else:
                i += 1
        else:
            if a[i] < b[j]:
                b.append(a[i])
                del a[i]
                j += 1
                i = 0
            else:
                i += 1

    return b


def even_greater_than_odd():
    a = [1, 2, 2, 1, 1, 2, 3, 4, 5, 6, 6, 5, 4]
    a = [1, 3, 2, 2, 5]

    for i in range(len(a)):
        if i % 2 == 0:
            if a[i] > a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
        else:
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]

    return a
