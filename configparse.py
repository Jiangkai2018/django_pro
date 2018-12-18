# -*- coding=utf-8 -*-
# configparser 主要用来操作解析配置文件的模块

import configparser
config = configparser.ConfigParser()   # 注意大小写

# 一，初始化实例
config.read('myconfig.ini')   # 配置文件的路径
# ["config.ini"]
# 或者直接初始化字典,
parser = configparser.ConfigParser()
dictobj = {'section1':{'key1':'value1'},'section2':{'key2':'value2'},}
parser.read_dict(dictobj)  # 这里如果用config.read_dict(dictobj) 就会在第一个解析器里追加这个字典内哦字典内容


# 查询
# 获取所有 sections
print(config.sections())
# 获取指定 section 的 keys
print(config.options('topsecret.com'))
# 获取指定 key 的 value
print(config['topsecret.com']['Port'])
print(config.get('bitbucket.org', 'User'))
print(config.getint('topsecret.com', 'Port'))


# 检查
print('DEFAULT' in config)
print('Tom' in config['bitbucket.org']['User'])

# 添加
config.add_section('mysection')
config.set('mysection', 'key_1', 'value_1')    # 注意键值是用set()方法
config.set('mysection', 'key_2', 'value_2')    # 注意键值是用set()方法
config.write(open('config.ini', 'w+'))    # 一定要写入才生效
print(config.sections()) # 已经陈公公写入

# 删除

config.remove_option('mysection', 'key_1')

print(config['mysection']['key_2'])

def f():
    """

    :param :none
    :return:
    """
    print('hello')
class cls(object):
    __doc__ = "这是一个测试类"
    def __init__(self):
        pass
cls().__doc__