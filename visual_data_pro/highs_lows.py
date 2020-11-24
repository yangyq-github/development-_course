#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/21 12:26
# @File  : highs_lows.py
__author__ = 'yangyanqin'

import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = "file_re/death_valley_2014.csv"

# first_date=datetime.strptime("2014-7-1","%Y-%m-%d")
# print(first_date)

with open(file_name) as f:
    reader = csv.reader(f)
    header_now = next(reader)

    # 从文件中获取日期和最高气温以及最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures - 2014 \n Death Valley,CA", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()

    # 打印文件头及其位置:
    # for index, colum_header in enumerate(header_now):  # enumerate()用来获取每个元素的索引和值
    #     print(index, colum_header)
