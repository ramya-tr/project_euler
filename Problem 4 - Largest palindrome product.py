def largest_palindrome_product():
    max_p = 1
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i*j

            if check_if_palindrome(str(product)) and product > max_p:
                max_p = product

    print(max_p)


def check_if_palindrome(str):

    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


largest_palindrome_product()