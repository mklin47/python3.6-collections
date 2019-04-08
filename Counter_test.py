#!usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter
# 在很多使用到dict和次数的场景下，Python中用Counter来实现会非常简洁，效率也会很高
users = ["mklin1", "mklin2", "mklin3", "mklin6", "mklin3", "mklin6"]
user_counter2 = Counter("abcdefg")  # 只要是可以迭代的对象
user_counter = Counter(users)
user_counter.update(user_counter2)  # 更新
print(user_counter.most_common(3))  # 前三
print(user_counter)
# 可以运行+ - & |