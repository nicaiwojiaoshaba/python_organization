
from functools import reduce

# lambda用法之高阶函数

'''
    map()函数
        map() 会根据提供的函数对指定序列做映射。
        语法：
            map(function, iterable, ...)
        参数：
            function ----> 函数
            iterable ----> 一个或多个序列
'''
print('map() 函数执行结果')
# 一般写法
def square(x):
    return x ** 2


map_result = map(square, [1, 2, 3, 4, 5])
print(list(map_result))

# 匿名函数写法
map_result = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(map_result))

map_result = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(map_result))

'''
    reduce() 函数
        reduce() 函数会对参数序列中元素进行累积。
        语法：
            reduce(function, iterable[, initializer])
        参数：
            function  ----> 函数，有两个参数
            iterable   ----> 可迭代对象
            initializer ----> 可选，初始参数
        返回值：
            返回函数计算结果。
'''
print('reduce() 函数执行结果')
# 一般写法
def add(x, y):
    return x + y


result = reduce(add, [1, 3, 5, 7, 9])
print(result)

# 匿名函数写法
result = reduce(lambda x, y: x + y, [1, 3, 5, 7, 9])
print(result)

'''
    sorted() 函数
        sorted() 函数对所有可迭代的对象进行排序操作。
        语法：
            sorted(iterable, key=None, reverse=False)
        参数说明：
            iterable  ----> 可迭代对象。
            key        ----> 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
            reverse  ----> 排序规则,reverse = True 降序, reverse = False 升序（默认）。
        返回值：
            返回重新排序的列表。

'''
# 简单用法
print('sorted() 函数执行结果')
list_a = [5, 7, 6, 3, 4, 1, 2]
list_b = sorted(list_a)
print(list_b)

# 匿名函数用法
old_list = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
new_list = sorted(old_list, key=lambda x: x[1])
print(new_list)

# 按照年龄排序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
new_students = sorted(students, key=lambda x: x[2])
print(new_students)

# 降序
new_students = sorted(students, key=lambda x: x[2], reverse=True)
print(new_students)

'''
    filter() 函数
        filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
        语法：
            filter(function, iterable)
        参数：
            function ----> 判断函数。
            iterable  ----> 可迭代对象。
        返回值：
            Pyhton2.7 返回列表,Python3.x 返回迭代器对象,具体内容可以查看:Python3 filter() 函数
'''
print('filter() 函数执行结果')
# 一般用法
def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))

# 匿名函数用法
# 将列表中能够被3整除的数过滤出来
newlist = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))
