def is_prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def prime(n):
    li = []
    for x in range(1, n + 1):
        if is_prime(x):
            li.append(x)
    return li
