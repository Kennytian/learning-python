d = {'Kenny': 100, '杰瑞': 80, '汤姆': 70}
print(d['Kenny'])

d['Emma'] = 23  # 可以用这种方式也能为dictionary添加key-value
print(d)  # {'Kenny': 100, '杰瑞': 80, '汤姆': 70, 'Emma': 23}

print('Kenny in d:', 'Kenny' in d)
print('\'Emma\' value', d.get('Emma'))
print('\'Jerry\' value', d.get('Jerry'))

print('pop Tom:', d.pop('汤姆'))  # 70
print(d)  # {'Kenny': 100, '杰瑞': 80, 'Emma': 23}

s = set([1, 2, 3])
print('set:', s)

s = set([1, 2, 3, 3, 4, 5, 5])
print('set:', s)  # 自动去掉重复项

s.add(6)
s.add(6)
print('set:', s)  # 重复项不会被添加进去

s1 = set([1, 2, 3])
s2 = set([1, 2, 4])
print('s1&s2:', s1 & s2)
print('s1|s2', s1 | s2)

s3 = set((1, 2, 3))
print('tuple in set3:', s3)


