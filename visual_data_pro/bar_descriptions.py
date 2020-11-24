#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/24 17:09
# @File  : bar_descriptions.py
__author__ = 'yangyanqin'

# 添加自定义工具提示
import pygal
from pygal.style import LightColorizedStyle as LCS

chart = pygal.Bar(style=LCS, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
