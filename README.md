## Python 学习

### 一、基础知识
#### 1.1 数据类型、变量、字符串和编码
1. Python 用 # 号作为注释，英文叫 octothorpe
2. Python 不使用 ; 号作为换行符
3. 两个 // 符号叫作地板除，结果不会有小数，如：`10 // 3  = 3`
4. Mac 上安装了 Python3，打开IDLE，就是 Python3 的环境
5. Mac 上安装了 Python3，在Terminal 里输入 `python3`，就是 Python3 的环境
6. 在 VSCode 里配置 Python3 环境，`Preferences` -> `Settings` -> 搜索 `python.pythonPath` -> 拷贝到 `User Settings` 里，将这一行改为 `"python.pythonPath": "python3"`,
7. pip 是 Python 上的包管理工具，类似于 NPM、Pod
8. Mac 上安装 pip 方法：`sudo easy_install pip`
9. 用 pip 安装包方法：`pip install autopep8`，或 `pip3 install autopep8`
10. 在 Python3 环境下安装pip包(不影响Python2)，如：`python3 -m pip install -U pylint`
11. Python 可以使用 autopep8 来自动排版为 PEP8 风格
12. 在 Python 文件第一行添加 `# coding: utf-8`，可防止乱码
13. Python 的转义字符与其它编程语言一样，用 \ 来表示
14. Python 允许用r''表示''内部的字符串默认不转义，如：print(r'\\\t\\')-> \\\t\\ 
15. Python 允许用'''...'''的格式表示多行内容
16. Python 布尔值只有True、False两种值，布尔值可以用and、or和not运算
17. Python 中 print("My score %d" % 4.5)，用%d输出4，改用%s输出4.5
18. Python 提供了 ord() 函数获取字符的整数表示，如：ord('中') # 20013
19. Python 提供了 chr() 函数把编码转换为对应的字符，如：chr(25991) # 文
20. Python 对 bytes 类型的数据用带b前缀的单引号或双引号表示，如：x = b'ABC'

#### 1.2 list 和 tuple
1. Python 内置数据类型是列表，list是一种有序的集合，可以随时添加和删除其中的元素
2. 初始化 classmates = ['Michael', 'Bob', 'Tracy']，取得列表长度(length) -> len(classmates)
3. 如果要取最后一个元素，除了计算索引位置外，还可以用`-1`做索引，直接获取最后一个元素 -> Tracy
4. list是一个可变的有序表，所以，可以往list中追加元素到末尾，如：`classmates.append('Adam')`
5. 把元素插入到指定的位置 classmates.insert(1, 'Jack') # ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
6. 要删除list末尾的元素，用pop()，如：classmates.pop() # ['Michael', 'Jack', 'Bob', 'Tracy']
7. 要删除指定位置的元素，用pop(i)方法，如：classmates.pop(1) # ['Michael', 'Bob', 'Tracy']
8. list里面的元素的数据类型也可以不同，L = ['Apple', 123, True]，s = ['a',['b','c'],'d']; len(s) # 3
9. tuple和list非常类似，但是tuple一旦初始化就不能修改，没有append()，insert()这样的方法
10. tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

#### 1.3 set 和 dict
1. set和dict类似，也是一组key的集合，但不存储value。由于key不能重复
2. 重复元素在set中自动被过滤，set([1, 1, 2, 2, 3, 3]) # {1, 2, 3}
3. set可以看成数学意义上的无序和无重复元素的集合，两个set可以做数学意义上的交集、并集等操作
```python
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2 # {2, 3}
s1 | s2 # {1, 2, 3, 4}
```
4. Python内部很地方都使用着dict这种结构，在对象属性dict就是一个字典，所以对其效率要求很高。

5. dict采用了**哈希表**，最低能在 o(1)时间内完成搜索，dict在发生哈希冲突的时候采用了**开放寻址法**。

#### 2. 参数
1. 在Python函数中，还可以定义可变参数，传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。如：`def calc(*numbers):`
2. 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误
3. *args 是可变参数，args 接收的是一个 tuple
4. **kw 是可变参数，kw 接收的是一个 dict


#### 文件操作
```
open(name, mode=None, buffering=None) 打开一个文件。
close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
read – 读取文件内容。你可以把结果赋给一个变量。
readline – 读取文本文件中的一行。
truncate – 清空文件，请小心使用该命令。
write(stuff) – 将stuff写入文件。
```

### Python 相关技能要求：
* 熟悉HTML CSS JavaScript
* 熟悉 MySQL、Oracle 等数据库
* 熟悉 Linux 
* 了解 HTTP 等网络协议
* 熟悉爬虫、数据分析
* 熟悉 Django、Flask、Tornado 等开发框架
* 熟悉树莓派设备 Python 开发
* 熟悉 RESTful 服务，深刻理解 MVC OOP
* 熟悉常用设计模式、微服务






