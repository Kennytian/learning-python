# conding: utf-8
names = ['Kenny', '杰瑞', '汤姆']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum+x
print(sum)

print(list(range(5)))

count = 0
for y in range(101):
    count = count + y
print(count)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if(n % 2 == 0):
        continue
    print(n)
