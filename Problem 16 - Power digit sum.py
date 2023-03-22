import time

def get_sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)

    return sum


def power_digit_sum():
    n = 2
    power = 1000
    number = pow(n, power)

    print(get_sum_of_digits(number))


def fewer_lines_of_code_approach():
    sum = 0
    for i in str(pow(2,1000)):
        sum += int(i)
    print(sum)


start_time = time.time()
power_digit_sum()
fewer_lines_of_code_approach()
print("--- %s seconds ---" % (time.time() - start_time))
