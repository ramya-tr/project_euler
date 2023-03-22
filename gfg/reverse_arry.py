def rev_ary():
    c = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
    a = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1, 19, 7, 0, 3, 18, 15, 12, 6, 1, -1]
    b = [-1]*len(a)

    # for i in range(len(a)):
    #     for i in range(len(a)):
    #         c[c[i]], c[i] = c[i], c[c[i]]
    #
    #     if a[i] != -1:
    #         b[a[i]] = a[i]

    i = 0
    c= a
    while i < len(c):
        if c[i] == -1:
            i += 1
        elif c[i] != i:
            if c[c[i]] != c[i]:
                c[c[i]], c[i] = c[i], c[c[i]]
            else:
                if c[c[i]] == i:
                    c[i] = -1
                elif c[i] < i:
                    c[i] = -1
                i += 1
        else:
            i += 1

    return c, sorted(a)
