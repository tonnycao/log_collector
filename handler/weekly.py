# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 13:33
# @Author  : Tonny Cao
# @Email   : 647812411@qq.com
# @File    : weekly.py
# @Software: PyCharm

import calendar
from config.config import *
from lib.mysql import ReportMySql
from lib.mysql import LanuchMySql


def get_month_range(year, month):
    return calendar.monthrange(year, month)


def get_month_calendar(year, month):
    return calendar.monthcalendar(year, month)

def week_days():
    # 9月份
    sde_week = [['2019-09-23','2019-09-29']]
    # 10
    otc_week = [['2019-09-30', '2019-10-06'], ['2019-10-07',  '2019-10-13'], ['2019-10-14',  '2019-10-20'],
                ['2019-10-21',  '2019-10-27'], ['2019-10-28',  '2019-11-03']]
    # 11
    sele_week = [['2019-11-04', '2019-11-10'], ['2019-11-11', '2019-11-17'], ['2019-11-18',  '2019-11-24']]
    week_days = [
        ['2019-09-23', '2019-09-29'],
        ['2019-09-30', '2019-10-06'],
        ['2019-10-07', '2019-10-13'],
        ['2019-10-14', '2019-10-20'],
        ['2019-10-21', '2019-10-27'],
        ['2019-10-28', '2019-11-03'],
        ['2019-11-04', '2019-11-10'],
        ['2019-11-11', '2019-11-17'],
        ['2019-11-18', '2019-11-24']
    ]
    return week_days

if __name__ == '__main__':
    '''
    [484, 632, 497, 591, 505, 528, 468, 553, 628]
    [446, 232, 326, 275, 180, 176, 209, 169, 125]
    
    [557, 703, 585, 681, 582, 621, 571, 666, 727]
    [460, 262, 370, 297, 198, 211, 237, 169, 196]
    '''
    # 9月份
    sde_week = [[23, 24, 25, 26, 27, 28, 29]]
    #10
    otc_week = [[30, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 1, 2, 3]]
    # 11
    sele_week = [[4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24]]
    start_date = '2019-09-23'
    end_date = '2019-11-23'
    weekday = start_date
    days_set = week_days()
    video_stats = []
    lanuch_stats = []
    report = ReportMySql(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_PORT, MYSQL_DB, MYSQL_CHARSET, 'tb_video_report')
    lanuch = LanuchMySql(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_PORT, MYSQL_DB, MYSQL_CHARSET, 'tb_launch_log')
    lanuch_num = 0
    video_num = 0
    s = 0
    for days in days_set:
        total = lanuch.state_by_date(days[0], days[1]+' 23:59:59')
        lanuch_stats.append(total)
        lanuch_num += total

        stat = report.state_by_date(days[0], days[1]+' 23:59:59')
        video_stats.append(stat)
        video_num += stat
        s += 1

    print(lanuch_stats)
    print(video_stats)
    print(lanuch_num/s)
    print(video_num/s)
