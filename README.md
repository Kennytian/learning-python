## Python 学习

### 一、基础知识
1. Python 用 # 号作为注释
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
12. 在 Python 文件第一行添加 `# -- coding: utf-8 --`，可防止乱码
