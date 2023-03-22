import time
from functools import reduce


def get_sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)

    return sum


def factorial_digit_sum():
    n = 100
    factorial = 1
    
    for i in range(100, 1, -1):
        factorial *= i
        
    print(get_sum_of_digits(factorial))


def fewer_lines_of_code_approach():
    print(reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))]))


start_time = time.time()
factorial_digit_sum()
fewer_lines_of_code_approach()
print("--- %s seconds ---" % (time.time() - start_time))
