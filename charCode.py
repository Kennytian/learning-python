# coding: utf-8
#!/usr/bin/env python3
# 字符编码
print('包含中文的str')
print(ord('A'))  # 函数获取字符的整数表示
print(ord('中'))
print(chr(66))  # 编码转换为对应的字符
print(chr(25991))
print('\u4e2d\u6587')  # 十六进制
print('ABC'.encode('ascii'))  # b'ABC'
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
print('中文'.encode('ascii', errors='ignore'))  # b''
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode())  # 中文
# 用errors='ignore'，允许部分转换成功
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print('ABC len: %d' % len('ABC'))  # ABC len: 3
print('中文 len: %d' % len('中文'))  # 中文 len: 2
print('b\'ABC\' len: %d' % len(b'ABC'))  # 中文 len: 3
print('b\'\\xe4\\xb8\\xad\\xe6\\x96\\x87 len: %d' %
      len(b'\xe4\xb8\xad\xe6\x96\x87'))  # b'\xe4\xb8\xad\xe6\x96\x87 len: 6
print('\'中文\'.encode(\'utf-8\') len: %d' %
      len('中文'.encode('utf-8')))  # '中文'.encode('utf-8') len: 6
print('%2d-%02d' % (3, 1))  # 3-01
print('%.2f' % 3.1415926)  # 3.14
