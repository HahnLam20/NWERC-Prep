#gcd
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

#lcm
def lcm(a, b):
    return (a*b)//gcd(a, b)

#extended euclid - updates results by using results calculated by recursive calls
def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclid(b%a, a)
    x = y1 - (b//a)*x1
    y = x1
    return gcd, x, y