#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/20 9:39
# @File  : scatter_squares.py
# __author__ = 'yangyanqin'
"""使用 scatter() 绘制散点图并设置其样式"""
import matplotlib.pyplot as plt
import numpy as np

x_values = list(range(1001))
y_values = [x ** 2 for x in x_values]

# 删除数据点的轮廓
plt.scatter(x_values, y_values, edgecolors='none', s=40, c=y_values,cmap=plt.cm.Blues)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)
# plt.tick_params(direction="out",which="major",zorder=" label zorder",width=8,length=10,color="red")

# 自动保存图表
plt.savefig('sqares_plot.png',bbox_inches='tight')

plt.show()
