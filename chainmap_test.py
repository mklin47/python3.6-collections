#!usr/bin/env python
# -*- coding:utf-8 -*-

from collections import ChainMap

user_dict1 = {"a": "mklin1", "b": "mklin2"}
user_dict2 = {"c": "mklin3", "d": "mklin4"}
new_dict = ChainMap(user_dict1, user_dict2)
new_dict = new_dict.new_child({"aa": "aa"})  # 添加新的节点
new_dict.update({"cc": "cc"})  # dict更新新的数据进去
print(new_dict.maps)
for key, value in new_dict.items():
    print(key, value)
user_dict1["ee"] = "EE"
print(new_dict.get("ee"))  # 获取某个值
print(new_dict.popitem())  # 弹出值最后一个插入的
print(new_dict)
