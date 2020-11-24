#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/21 11:55
# @File  : different_dice.py
__author__ = 'yangyanqin'

"""同时掷两个面数不同的骰子"""

import pygal
from visual_data_pro.die import Die

# 创建一个D6和一个D10
die_01 = Die()
die_02 = Die(10)

# 掷骰子多次,并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_01.roll() + die_02.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_01.num_sides + die_02.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()
hist.title = "Result of rolling a D6 and a D10 50,000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10', frequencies)
hist.render_to_file('different_visual.svg')
