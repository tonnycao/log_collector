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
        self.proc = None
        self.metadata = dict()

    def _scan(self):
        '''
        开始
        :return:
        '''
        result = None
        cmd = 'tail  -n 10  -f%s'.format(self.path)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, encoding='utf-8')
        self.proc = proc

    def parse_line(self):
        '''
        处理函数
        :return:
        '''
        line = self.proc.stdout.readline().rstrip()
        data = self.instance.parse(line)

    def run(self):
        self._scan()
        self.t = Timer(self.scan_frequency, self.parse_line)
        self.t.start()




