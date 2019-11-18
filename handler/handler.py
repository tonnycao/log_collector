# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 14:32
# @Author  : Tonny Cao
# @Email   : 647812411@qq.com
# @File    : handler.py
# @Software: PyCharm
import re


class Handler(object):
    path = ''
    when = 'H'

    def __init__(self, path, when=None):
        self.path = path
        if when is not None:
            self.when = when

    def parse_nginx(self):
        '''
        分析ngixn访问日志
        :param log_path:日志文件
        :return: []
        '''

        url_list = []
        fd = open(self.path, mode='r', encoding='utf-8')
        for line in fd.readlines():
            content = line.strip()
            p1 = content.index(']') + 1
            ip_time = content[0:p1]
            left_part = content[p1 + 1:].strip()
            left_parts = left_part.split('"')
            method = left_parts[1]
            status = left_parts[2].strip()
            user_agent = left_parts[5]
            ip_times = ip_time.split(' ')
            ip = ip_times[0]
            time_str = ip_times[3].strip('[')
            url = ''
            mac = ''
            p2 = user_agent.find('MAC')
            if p2 > 0:
                mac = user_agent[p2 + 4:]
            methods = method.split(' ')
            device = ''
            reg1 = re.compile(r'[(](.*?)[)]', re.S)
            devices = re.findall(reg1, user_agent)
            if len(devices) > 0:
                device = devices[0]
            data = {
                'ip': ip,
                'time': time_str,
                'method': methods[0],
                'url': methods[1].strip(),
                'status': status,
                'user_agent': user_agent,
                'mac': mac,
                'device': device
            }
            url_list.append(data)

        return url_list

    def parse_video(self):
        stats = []
        fd = open(self.path, mode='r', encoding='utf-8')
        for line in fd.readlines():
            line = line.strip()
            lines = line.split(',')
            item = dict()

            contents = lines[4].split(':')
            if len(contents) == 2:
                if contents[1].endswith('.mp4') is True or contents[1].endswith('.ts') is True:
                    times = lines[0].split(':')
                    ips = lines[2].split(':')
                    time = times[1].replace('[', '')
                    time = time.replace(']', '')
                    item['content'] = contents[1]
                    item['time'] = time
                    item['ip'] = ips[1]
            if len(item)>0:
                stats.append(item)
        return stats

