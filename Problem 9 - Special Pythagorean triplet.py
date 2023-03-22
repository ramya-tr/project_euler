import time

# brute force
def special_pythagorean_triplet():
    number = 1000

    for i in range(number, 0, -1):
        for j in range(number, 0, -1):
            for k in range(number, 0, -1):
                if (i+j+k) == number:
                    if pow(i, 2) + pow(j, 2) == pow(k, 2):
                        print(i, " ", j, " ", k)
                        print("product: ", (i * j * k))
                        return

# better approach
'''
For all triples, a^2+b^2 = c^2; 
a+b > c, c > a, c > b. 
We can also define b > a.
Since a + b + c = 1000, it follows that 500 > c > 334. 
(If c > 500, then a+b > c doesn't hold. If c < 334 and b > a, then c > b doesn't hold.)
'''

def special_pythagorean_triplet_better_approach():
    number = 1000

    for c in range(334, 500):
        for a in range(1, (1000 - c) // 2):
            b = (1000 - c) - a
            if a ** 2 + b ** 2 == c ** 2:
                print("a,b,c =", a, b, c)
                print("product: ", (a*b*c))
                return


start_time = time.time()
# special_pythagorean_triplet()
special_pythagorean_triplet_better_approach()
print("--- %s seconds ---" % (time.time() - start_time))
