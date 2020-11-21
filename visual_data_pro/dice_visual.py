#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/20 16:11
# @File  : dice_visual.py
__author__ = 'yangyanqin'

"""同时掷两个骰子"""

import pygal
from visual_data_pro.die import Die

# 创建两个D6的骰子
die_1 = Die()
die_2 = Die()
# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = "Result of rolling two D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Frequencies of Result"

hist.add("D6+D6", frequencies)
hist.render_to_file("dice_visual.svg")
