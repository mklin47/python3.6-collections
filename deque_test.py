#!usr/bin/env python
# -*- coding:utf-8 -*-
from collections import deque

user_deque = deque(["mklin", 30, 175])  # list set dict（以key值） tuple 都可以
user_deque.append("test")  # 右插入
user_deque.appendleft("haha")  # 左插入
user_deque2 = user_deque.copy()  # 拷贝
user_deque.remove(30)  # 删除具体的值
user_deque.clear()  # 清除所有数据
print(user_deque2.count(175))  # 统计指定值的个数
user_deque2.extend(["fuck", "deque"])  # 左插入多个数据
user_deque2.extendleft(("hualao", "kao"))  # 右插入多个数据
print(user_deque2.index("fuck"))  # 查找指定值在deque中的位置
user_deque2.insert(0, "tmd")  # 指定位置插入数据
print(user_deque2.pop())
print(user_deque)
print(user_deque2)
user_deque2.reverse()
print(user_deque2)
