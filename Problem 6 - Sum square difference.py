def sum_of_n_natural_numbers(n):
    return (n*(n+1))/2


def sum_of_square_of_n_natural_numbers(n):
    return (n*(n+1)*((2*n)+1))/6


def sum_square_difference():
    n = 100
    square_of_sum_of_n_natural_numbers = pow(sum_of_n_natural_numbers(n), 2)
    sum_of_the_square_of_n_natural_numbers = sum_of_square_of_n_natural_numbers(n)

    print( abs(sum_of_the_square_of_n_natural_numbers-square_of_sum_of_n_natural_numbers))

sum_square_difference()