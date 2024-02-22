import random
'''
    在字典中提取或者修改数据，返回新的字典
'''
dictionary_1 = {'a': '1234', 'B': 'FFFF', 'c': ' 23432', 'D': '124fgr', 'e': 'eeeee', 'F': 'QQQQQ'}
# 案例一:获取字典中key值是小写字母的键值对
# 预期结果:{'a': '1234', 'c': ' 23432', 'e': 'eeeee'}
dictionary_2 = {key: value for key, value in dictionary_1.items() if key.islower()}
print(dictionary_2)
# 案例二:将字典中的所有key设置为小写,value值设置为大写
# 预期结果:{'a': '1234', 'b': 'FFFF', 'c': ' 23432', 'd': '124FGR', 'e': 'EEEEE', 'f': 'QQQQQ'}
dictionary_2 = {key.lower(): value.upper() for key, value in dictionary_1.items()}
print(dictionary_2)
# 案例三:将字典中所有key是小写字母的value统一赋值为'error'
# 预期结果:{'a': 'error', 'B': 'FFFF', 'c': 'error', 'D': '124fgr', 'e': 'error', 'F': 'QQQQQ'}
dictionary_2 = {key: value if not key.islower() else 'error' for key, value in dictionary_1.items()}
print(dictionary_2)
'''
    在字符串中提取数据，返回新的字典:
    预期结果:{'anonymid': 'jy0ui55o-u6f6zd', ' depovince': 'GW', ' _r01_': '1', ' JSESSIONID': 'abcMktGLRGjLtdhBk7OVw', ' ick_login': 'a9b557b8-8138-4e9d-8601-de7b2a633f80'}
'''

# 在爬虫中，我们需要获取cookies并以字典的形式传参，如果cookies是字符串则需要转换为字典，经典代码案例如下:
# 原来的cookies很长，这里截取一部分做演示:

cookies = "anonymid=jy0ui55o-u6f6zd; depovince=GW; _r01_=1; JSESSIONID=abcMktGLRGjLtdhBk7OVw; ick_login=a9b557b8-8138-4e9d-8601-de7b2a633f80"

# 字典推导式，将长的字符串转化为字典。
cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split(';')}
print(cookies_dict)
cookies_dict = {key: value for cookie in cookies.split(';') for key, value in (cookie.split('='),)}
print(cookies_dict)
'''
    将字符串 "k:1|k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}:
    预期结果:{'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
'''
str = "k:1|k1:2|k2:3|k3:4"
str_dict = {item.split(":")[0]: item.split(":")[1] for item in str.split("|")}
print(str_dict)
str_dict = {key: value for item in str.split("|") for key, value in (item.split(":"),)}
print(str_dict)
'''
    生成一个包含5个随机数的字典:
    预期结果:{1: 随机数, 2: 随机数, 3: 随机数, 4: 随机数, 5: 随机数}
'''
new_dict = {i: random.randint(0, 100) for i in range(1, 6)}
print(new_dict)
'''
    将两个长度相同的列表合并成字典:
    预期结果:{'zhangsan': '双鱼座', 'lisi': '天蝎座', 'wangwu': '水瓶座', 'maliu': '巨蟹座'}
'''
name = ['zhangsan', 'lisi', 'wangwu', 'maliu']
sign = ['双鱼座', '天蝎座', '水瓶座', '巨蟹座']

new_dict = {key: value for key, value in zip(name, sign)}
print(new_dict)

'''
    将字典中key、value互换位置:
    预期结果:{'a': 1, 'b': 2, 'c': 3}
'''
d = {1: 'a', 2: 'b', 3: 'c'}
new_dict = {value: key for key, value in d.items()}
print(new_dict)
