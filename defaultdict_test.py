#!usr/bin/env python
# -*- coding:utf-8 -*-
from collections import defaultdict
# 使用场景统计users中的重复值的个数
users = ["hahaxiao", "ganlanzhi", "mklin1", "mklin2", "mklin1", "mklin2"]
# 通常做法1，容易漏掉判断,效率不高
user_dict = {}
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] += 1  # 报错KeyError
# 做法2
user_dict = {}
for user in users:
    user_dict.setdefault(user, 0)  # 解决key默认值，setdefault是dict内置的(效率比not in更高)
    user_dict[user] += 1
# 做法3，推荐
user_dict = defaultdict(int)  # 传入默认值类型
for user in users:
    user_dict[user] += 1

# 高级用法嵌套dict
def gen_default():
    return {
        "name": "",
        "nums": 0
    }
user_dict = defaultdict(gen_default)
user_dict["group1"]
pass
