# Python3 program to rearrange an
# array in minimum maximum form

# Prints max at first position, min at second position
# second max at third position, second min at fourth
# position and so on.

def segregate_odd_even1():
    a = [1, 3, 2, 4, 7, 6, 9, 10]

    return [i for i in a if i % 2 == 0] + [i for i in a if i % 2 == 1]


def segregate_odd_even():
    a = [2, 4, 6, 8, 1, 3, 2, 4, 7, 6, 9, 10]

    index = 0

    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i], a[index] = a[index], a[i]
            index+=1

    return a
