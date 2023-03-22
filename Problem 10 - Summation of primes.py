import time

def is_prime_number(number, prime_number_list):
    factor = 1

    for i in prime_number_list:
        if number%i == 0:
            return False

    return True


def summation_of_primes():
    n = 2000000
    sum = 2
    number = 3
    prime_number_list = []

    while number < n:
        if is_prime_number(number, prime_number_list):
            sum += number
            prime_number_list.append(number)
        number += 2

    print(sum)

def prime_using_sieve():
    n = 2000000
    sum = 2
    number = 3
    sieve_list = [0] * n

    while number < n:
        if sieve_list[number] == 0:
            sum += number
            i = number*2
            while i < n:
                sieve_list[i] = 1
                i += number
        number += 2

    print(sum)
                


start_time = time.time()
# summation_of_primes()
prime_using_sieve()
print("--- %s seconds ---" % (time.time() - start_time))
