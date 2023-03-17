def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binomial(n, p, k):
    comb = factorial(n) // (factorial(k) * factorial(n-k))
    return comb * p**k * (1-p)**(n-k)

def poisson(lam, k):
    import math
    e = math.exp(1)
    return (lam ** k / math.factorial(k)) * e ** (-lam)

def gaussiana(x, mu, sigma):
    import math
    return math.exp(-(x - mu)**2 / (2 * sigma**2)) / (sigma * math.sqrt(2 * math.pi))
