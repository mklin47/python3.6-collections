#!usr/bin/env python
# -*- coding:utf-8 -*-
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合tuple1 + tuple2
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
name_tuple = ('hahaxiao', 'ganlanzhi')
old_id = id(name_tuple)
name_tuple = ('hahaxiao2', 'ganlanzhi2')  # name_tuple只是一个名称指向内存区块
new_id = id(name_tuple)
print(old_id == new_id)  # 内存区域新开了一个区块放置内容，把name_tuple指向新的区块
for name in name_tuple:  # tuple可以迭代遍历
    print(name)
# name_tuple[1] = 'text change'  # TypeError: 'tuple' object does not support item assignment
tuple_tuple2 = ('mklin', 30, [1, 2, 3], {'tt': 'hah'})  # 不推荐在tuple中保存可变对象
print(tuple_tuple2)
tuple_tuple2[2][0] = 'list chagne'  # tuple不可变性不是绝对的（tuple中的list是可变的）
print(tuple_tuple2)

name, age, *other = tuple_tuple2  # 拆包
print(name, age, other)  # other保存多余的参数在一个list中
print("{0}---{1}".format('text', 'ganlanzhi'))
print("%s:%d" % ("你好", 8))  # 格式化字符串
user_info_dict = {}
user_info_dict[name_tuple] = 'mklin'  # tuple可以作为dict的key值，是因为tuple可以hash
print(user_info_dict)
user_info_dict[[1, 2, 3]] = 'fffg'  # TypeError: unhashable type: 'list'
