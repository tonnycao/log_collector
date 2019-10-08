# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 15:59
# @Author  : Tonny Cao
# @Email   : 647812411@qq.com
# @File    : api.py
# @Software: PyCharm
from config.config import *
import pprint

def stat_video_log(file):
    data = set()
    fd = open(file, 'r', encoding='utf-8')
    for line in fd.readlines():
        if len(line)>0:
            line = line.strip()
            content = line.split(',')
            if content[4] is not None:
                contents = content[4].split(':')
                data.add(contents[1])
    return data

def stat_video_dir(path):
    pass

if __name__ == '__main__':
    log = DATA_PATH + '/2019-09-23.log'
    result = stat_video_log(log)
    pprint.pprint(result)