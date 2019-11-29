# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 9:59
# @Author  : Tonny Cao
# @Email   : 647812411@qq.com
# @File    : markdown2html.py
# @Software: PyCharm
import re
import os
import markdown
from config.config import *


def replace_md2html(file_path):
     '''
     内链md 修改成html
     内嵌html 转义
     :param file_path:
     :return:
     '''
     with open(file_path, mode='r', encoding='utf-8') as fhandle:
          str_url = fhandle.read()
          pattern = re.compile(r'<a href=".*?">')
          search_result = pattern.findall(str_url)
          maohao = re.compile(r'".*?"')
          data = []
          for i in search_result:
               result = maohao.findall(i)
               tmp = result[0].replace("\"", "")
               if not tmp.startswith('http'):
                    old_path = tmp
                    tmp = tmp.replace("../", "")
                    tmps = tmp.split('/')
                    print(old_path)
                    dir_name = format_name(tmps[0])
                    file_name = format_name(tmps[1])
                    new_path = '/' + dir_name + '/' + file_name + '.html'
                    print(new_path)
                    data.append(new_path)
     return data

def format_name(file_name):
     result = re.split('\W+', file_name)
     name = ''
     for i in result:
          if i.isdigit():
               name += '.' + i
          if i != 'md' and i.isdigit() is False:
               name = name.lstrip('.')
               name += '-' + i
     result = name.rstrip('-').lower()
     result = result.lstrip('-')
     return result

def mk2html(file_path, out_dir):
     with open(file_path, mode='r', encoding='utf-8') as fhandle:
          readme_content = fhandle.read()
          if readme_content and len(readme_content)>0:
               file_names = file_path.split(os.path.sep)
               file_name = file_names[len(file_names)-1].replace('.md', '')
               del file_names[len(file_names)-1]
               name = format_name(file_name)
               file_dir = os.path.sep.join(file_names)
               html = markdown.markdown(readme_content)
               html_file = out_dir + os.path.sep + name + '.html'
               html_handle = open(html_file, mode='w+', encoding='utf-8')
               html_handle.write(html)
               replace_md2html(html_file)

def main():
     dir_names = os.listdir(DATA_PATH + os.path.sep + "Spring-Boot-Reference-Guide")
     result_dir = DATA_PATH + os.path.sep + 'html'
     for dir_item in dir_names:
          file_dir = DATA_PATH + os.path.sep + "Spring-Boot-Reference-Guide" + os.path.sep + dir_item + os.path.sep
          file_names = [name for name in os.listdir(file_dir)
                   if os.path.isfile(os.path.join(file_dir, name)) and name.endswith('.md')]
          if len(file_names)>0:
               for file_name in file_names:
                    file_path = os.path.join(file_dir, file_name)
                    dir_name = format_name(dir_item)
                    out_dir = result_dir + os.path.sep + dir_name + os.path.sep
                    is_exists = os.path.exists(out_dir)
                    if not is_exists:
                         os.makedirs(out_dir)
                    mk2html(file_path, out_dir)

if  __name__ == '__main__':
   main()
