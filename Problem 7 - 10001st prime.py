import time

def is_prime_number(number, prime_number_list):
    factor = 1

    for i in prime_number_list:
        if number%i == 0:
            return False

    return True


def n_th_prime_number():
    n = 10001
    count = 1
    number = 3
    prime_number_list = []

    while count < n:
        if is_prime_number(number, prime_number_list):
            count +=1
            prime_number_list.append(number)
        number += 2

    print(number-2)

start_time = time.time()
n_th_prime_number()
print("--- %s seconds ---" % (time.time() - start_time))
