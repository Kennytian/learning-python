# coding: utf-8
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


# 指定参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print('[1,2,3] -> %s' % calc([1, 2, 3]))
print('(1,3,5,7) -> %s' % calc((1, 3, 5, 7)))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print('2, 4, 6 -> %s' % calc(2, 4, 6))
print('() -> %s' % calc())
print('*[1, 2, 3] -> %s' % calc(*[1, 2, 3]))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Kenny', 30)  # ('name:', 'Kenny', 'age:', 30, 'other:', {})

person('Tom', 20, city='England')  # ('name:', 'Tom', 'age:', 20, 'other:', {'city': 'England'})

person('Adam', 45, gender='M', job='Engineer')  # ('name:', 'Adam', 'age:', 45, 'other:', {'gender': 'M', 'job': 'Engineer'})

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 23, **extra)  # ('name:', 'Jack', 'age:', 23, 'other:', {'city': 'Beijing', 'job': 'Engineer'})
