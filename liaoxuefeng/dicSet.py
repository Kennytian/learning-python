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
