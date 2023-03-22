def primeFactor(number):
    factor = 1
    print(number)

    for i in range(2, (number//2)+1):
        if number%i == 0:
            factor = i

    if factor == 1:
        return True

    return False

def largestPrimeFactor(number):
    factor = 1

    for i in range(3, (number//2)+1, 2):
        if number%i == 0 and primeFactor(i) == 1:
            factor = i

    print(factor)

def factoriseMethod(number):
    factor = 2
    original_number = number
    prime_factor = 1
    while factor*factor < original_number:
        if number % factor == 0:
            number = number//factor
            prime_factor=factor
        else:
            factor = factor + 1

    print(prime_factor)


number = 600851475143
# largestPrimeFactor(number)
factoriseMethod(number)


