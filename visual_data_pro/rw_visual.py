#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/20 14:59
# @File  : rw_visual.py
__author__ = 'yangyanqin'

import matplotlib.pyplot as plt
from visual_data_pro.random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来

# 只要程序处于活动状态，就不断地模拟随机漫步

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 调整适合屏幕大小的尺寸
    plt.figure(figsize=(10,6))

    # 给点着色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors="none", s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
