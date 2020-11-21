#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/20 15:25
# @File  : die.py
__author__ = 'yangyanqin'

from random import  randint

class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        """骰子默认是6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1,self.num_sides)