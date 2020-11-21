#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/20 15:28
# @File  : die_visual.py
__author__ = 'yangyanqin'

import pygal
from visual_data_pro.die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

print(results)

# 分析结果:把每个数字出现的次数，以字典的方式打印出来
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    # 如果未出现的数字，则选择不打印
    # if frequency != 0:
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1, 7)]
hist.x_title = "Result"
hist.y_tile = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")
