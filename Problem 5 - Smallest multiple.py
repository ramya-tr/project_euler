def factors_of_a_number(number):
    factor = 2
    original_number = number
    prime_factor = {}

    while factor <= original_number:
        if number % factor == 0:
            number = number//factor
            prime_factor[factor] = prime_factor.get(factor,0)+1
        else:
            factor = factor + 1

    return prime_factor


def smallest_multiple():
    prime_factors = {}

    for i in range(2, 21):
        factors_dict = factors_of_a_number(i)
        for factor, count in factors_dict.items():
            if factor in prime_factors.keys():
                prime_factors[factor] = max(prime_factors[factor], count)
            else:
                prime_factors[factor] = count

    product = 1
    for factor, count in prime_factors.items():
        product = product * pow(factor, count)

    print(product)

smallest_multiple()