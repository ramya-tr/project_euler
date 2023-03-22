import time

def get_number_of_factors_of_a_number(num):
    factors_set = {1, num}
    max_num_to_check_till = round(pow(num, (1/2)))

    for i in range(2, max_num_to_check_till):
        # if i >= max_num_to_check_till:
        #     break

        if num%i == 0:
            factors_set.add(i)
            factors_set.add(num/i)
            max_num_to_check_till = num/i

    return len(factors_set)


def highly_divisible_triangular_number():
    highest_num_of_divisors = 500
    triangular_number = 1
    natural_number_series = 2

    while True:
        triangular_number += natural_number_series

        if triangular_number > (highest_num_of_divisors*2):
            if get_number_of_factors_of_a_number(triangular_number) >= highest_num_of_divisors:
                print(triangular_number)
                return

        natural_number_series += 1



start_time = time.time()
highly_divisible_triangular_number()
print("--- %s seconds ---" % (time.time() - start_time))
