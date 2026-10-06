def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

# print(gcd(7, 9))
# print(gcd(8, 64))
# print(gcd(15, 25))
# print(gcd(0, 25))
# print(gcd(6, 0))