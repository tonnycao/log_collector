# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 15:24
# @Author  : Tonny Cao
# @Email   : 647812411@qq.com
# @File    : filebeater.py
# @Software: PyCharm
import subprocess
from subprocess import TimeoutExpired
from threading import Timer


class FileBeater(object):

    def __init__(self, instance, path, ext, scan_frequency=10, include_fields=None, exclude_fields=None, shutdown_timeout=-1):
        '''
        初始化
        :param path: 路径
        :param ext: 后缀
        :param scan_frequency: 频率
        :param include_fields: 包含字段
        :param exclude_fields: 过滤字段
        :param shutdown_timeout: 超时时间
        '''
        self.path = path
        self.ext = ext
        self.scan_frequency = scan_frequency
        self.include_fields = include_fields
        self.exclude_fields = exclude_fields
        self.shutdown_timeout = shutdown_timeout
        self.instance = instance
        self.count = 0
        self.t = None

    def scan(self):
        '''
        开始
        :return:
        '''
        result = None
        cmd = 'tail  -n 1  -f%s'.format(self.path)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        try:
            outs, errs = proc.communicate(timeout=15)
        except TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
        if outs:
            result = self.parse_line(outs)
            self.count += 1
        return result

    def parse_line(self, line):
        '''
        处理函数
        :return:
        '''
        data = self.instance.parse(line)
        return data

    def run(self):
        self.t = Timer(self.scan_frequency, self.scan)
        self.t.start()




