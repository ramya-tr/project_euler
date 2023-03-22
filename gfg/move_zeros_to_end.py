def move_zeros_to_end1():
    a = [1, 2, 0, 4, 3, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 5, 0]

    n = 0

    last_zero_index = len(a) - 1

    for i in range(last_zero_index, -1, -1):
        if a[i] == 0:
            last_zero_index = i
            break

    while n <= last_zero_index:
        if a[n] == 0 and n < last_zero_index:
            for i in range(n+1, len(a)):
                if a[i] != 0:
                    a[i], a[n] = a[n], a[i]
                    # n = i
                    break
            last_zero_index -= 1
        # else:
        n += 1

    return a


def move_zeros_to_end():
    a = [1, 2, 0, 4, 3, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 5, 0]

    j = 0
    for i in range(len(a)-1):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1

    return a
