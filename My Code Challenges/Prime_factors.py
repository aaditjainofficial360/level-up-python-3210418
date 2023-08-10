def get_prime_factors(number):
    factors = []
    prime_factors = []
    flag = True
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    for j in factors[1:]:
        for k in range(2, j):
            if j % k == 0:
                flag = False
        if flag:
            prime_factors.append(j)
    return prime_factors


print(get_prime_factors(14))
print(get_prime_factors(45))
print(get_prime_factors(67))
print(get_prime_factors(93))
print(get_prime_factors(60))