#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/17 15:48
# @File  : alien_invasion.py
__author__ = 'yangyanqin'

import pygame, sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(__file__)))

from alien_invasion.settings import Settings
print(Settings().screen_height)
# def run_game():
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption(ai_settings.game_title)
#
#     # 设置背景色
#     bg_color = (ai_settings.bg_color)
#
#     # 开始游戏的主循环
#     while True:
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(bg_color)
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()


# run_game()
