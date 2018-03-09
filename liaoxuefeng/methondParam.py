def power(x):
    return x * x


print('%d x %d = %d' % (3, 3, power(3)))


def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


def power2(x, n=2):
    s = 1
    for i in range(n):
        s = s * x
    return s


print(power(5, 5))

print(power2(5, 5))

print(power2(3))


def addEnd(L=[]):
    L.append('End')
    return L


print(addEnd([1, 2, 3]))


def addEnd(L=None):
    if L is None:
        L = []
    L.append('End')
    return L

print(addEnd())