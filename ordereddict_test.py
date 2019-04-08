#!usr/bin/env python
# -*- coding:utf-8 -*-

from collections import OrderedDict
# 生成有序字典
user_dict = OrderedDict()
user_dict['d'] = 'D'
user_dict['a'] = "A"
user_dict['b'] = 'B'
user_dict['c'] = 'C'
user_dict.move_to_end("d")  # 移动到末尾
print(user_dict.popitem())  # 弹出最后一个元素
print(user_dict)
print(user_dict.keys())  # dict key值
print(user_dict.items())  # 键值对
print(user_dict.values())  # 所有值
user_dict2 = user_dict.copy()  # 浅拷贝
user_dict2['a'] = "AA"
print(user_dict, user_dict2)
