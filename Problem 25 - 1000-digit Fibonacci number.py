import time

def get_next_fibonacci_number():
    a = 1
    b = 1

    while True:
        a, b = b, (a+b)
        yield b



def thousand_digit_fibonacci_number():
    size = 1000
    fibonacci = get_next_fibonacci_number()
    count = 3
    
    while True:
        next = fibonacci.__next__()
        if len(str(next)) == size:
            print(count)
            break

        count += 1



start_time = time.time()
thousand_digit_fibonacci_number()
print("--- %s seconds ---" % (time.time() - start_time))
