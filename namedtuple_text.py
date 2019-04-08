# -*- coding: utf-8 -*-
from collections import namedtuple

# Python元组的升级版本 -- namedtuple(具名元组)
# 因为元组的局限性：不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义，所以在这里引入了
#  collections.namedtuple 这个工厂函数，来构造一个带字段名的元组。具名元组的实例和普通元组消耗的内存一样多，
# 因为字段名都被存在对应的类里面。这个类跟普通的对象实例比起来要小一些，因为Python不会用 __dict__ 来存放这些实例的属性。
# namedtuple比tuple具有更多的好处，减少内存开销
# tuple使用下标来访问，namedtuple使用字典通过名字进行访问，只不过其中的值是不能改变的
# namedtuple生成可以使用名字来访问元素内容的tuple子类
# namedtuple主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性,在访问一些tuple类型的数据时尤其好用。
# user表的数据全部取出然后增加一个列
User = namedtuple("UserInfo", ["name", "age", "height", "edu"])
user_tuple = ('mklin', 30, 174)
user_dict = {
    "name": "mklin2", "age": 32, "height": 175
}
user = User(*user_tuple, "zc")  # 可变参数
user = User(**user_dict, edu="zcxy")  # 关键字参数
print(user.name, user.age, user.height, user.edu)  # 获取用户的属性
print(user._replace(age=22))  # 修改属性值
print(user._asdict())  # 转字典
print(user._fields)  # 所有字段
# _class_template模版字符串生成类（继承tuple）
user2 = User._make(["mklin", 32, 175, "fzzc"])  # 需要传入一致的参数(不够灵活)
print(user2)
