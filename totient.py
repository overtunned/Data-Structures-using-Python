def tot(n) :
    result = n
    p = 2
    while p <= n**0.5 :

        if n % p == 0 :
            result = result * (1.0 - (1.0 / float(p)))
            while n % p == 0 :
                n = n // p
        p = p + 1
        
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n)))

    return int(result)

for n in range(1, 11) :
    print("tot(", n, ") = ", phi(n))
