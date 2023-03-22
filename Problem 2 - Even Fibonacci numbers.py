def evenFibonacciNumbers():
    limit = 4000000

    a,b, sum = 1,2,0
    while a < limit and b < limit:
        if b%2 == 0:
            sum+=b

        a,b = b, a+b

    print(sum)

evenFibonacciNumbers()