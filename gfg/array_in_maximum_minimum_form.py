"""
Given a sorted array of positive integers, rearrange the array alternately i.e first element should be a maximum value, at second position minimum value, at third position second max, at fourth position second min, and so on.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: arr[] = {7, 1, 6, 2, 5, 3, 4}

Input: arr[] = {1, 2, 3, 4, 5, 6}
Output: arr[] = {6, 1, 5, 2, 4, 3}
"""

def array_in_maximum_minimum_form():
    a = [1, 2, 3, 4, 5, 6, 7]
    a = [1, 2, 3, 4, 5, 6]
    o = []
    j = 0

    while j <= len(a)//2 - 1:
        o.append(a[len(a)-1-j])

        if j < len(a)//2:
            o.append(a[j])

        j+=1

    if len(a) % 2 == 1:
        o.append(a[len(a)//2])

    return o
