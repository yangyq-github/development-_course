#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/21 14:34
# @File  : btc_close_2017.py
__author__ = 'yangyanqin'

# from  __future__ import (absolute_import,division,print_function,unicode_literals)

try:
    # Python 2.x 版本
    from urllib2 import urllib
except ImportError:
    # Pythoe 3.x 版本
    from urllib.request import urlopen

import json, pygal
from itertools import groupby

# 从文件中读取数据
with open("file_re/btc_close_2017.json") as f:
    bt_data = json.load(f)

# 创建5个列表,分别存储日期和收盘价
dates, months, weeks, weekdays, closes = [], [], [], [], []

# 打印每一天的心
for btc_dict in bt_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = (btc_dict['close'])
    dates.append(date)
    months.append(month)
    weeks.append(int(week))
    weekdays.append(weekday)
    closes.append(int(float(close)))
    # print("{} is month {} week {},{},the close price is {} RMB".format(date, month, week, weekday, close))

# 绘制收盘价折线图
line_chart = pygal.Line(x_label_rotation=20,
                        show_minor_x_labels=False)  # x_label_rotation让x轴上的日期标签顺时针旋转20度,show_minor_x_labels不用显示所有的x轴标签
line_chart.title = "收盘价(￥)"
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', closes)


# line_chart.render_to_file("收盘价折线图(￥).svg")


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []

    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda __: __[0]):
        y_list = [v for _, v in y]
        xy_map.append([str(x), sum(y_list) / len(y_list)])

    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


# 收盘价月日均值
idx_month = dates.index('2017-12-01')
# line_chart_month = draw_line(months[:idx_month], closes[:idx_month], "收盘价月日均值（￥）", '月日均值')

# 收盘价周日均值
idx_week = dates.index("2017-12-11")
# line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值（￥）', "周日均值")

wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week], "收盘价星期均值（￥）", "星期均值")
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# line_chart_weekday.render_to_file("收盘价星期均值（￥）.svg")


# 收盘价数据仪表盘
with open('收盘价Dashboard.html', 'w', encoding='utf-8')  as  html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图(￥).svg', '收盘价对数变换折线图（¥）.svg', '收盘价月日均值（￥）.svg',
        '收盘价周日均值（￥）.svg', '收盘价星期均值（￥）.svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')


