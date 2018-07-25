# coding:utf-8

'''
@author = super_fazai
@File    : json_utils.py
@Time    : 2018/7/25 09:43
@connect : superonesfazai@gmail.com
'''

__all__ = [
    'read_json_from_local_json_file',                       # 从本地json文件读取json, 并以dict返回
]

def read_json_from_local_json_file(json_file_path):
    '''
    从本地json文件读取json, 并以dict返回
    :param json_file_path:
    :return: a dict
    '''
    from ..common_utils import json_2_dict

    try:
        result = ''
        with open(json_file_path, 'r') as file:
            for item in file.readlines():
                result += item.replace('\n', '')
    except FileNotFoundError as e:
        print('json path 文件不存在, 请检查!')
        raise e

    # print(result)
    _ = json_2_dict(json_str=result)

    return _





