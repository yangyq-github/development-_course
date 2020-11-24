#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/24 15:58
# @File  : python_repos.py
__author__ = 'yangyanqin'

# 执行API调用并存储响应
import requests, pygal
from pygal.style import LightColorizedStyle as LCS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# names, stars = [], []
names, plot_dicts = [], []
print("Repositories returned:", len(repo_dicts))

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
    # plot_dicts.append(repo_dict['stargazers_count'])

    # print("\nName：", repo_dict['name'])
    # print("Owner：", repo_dict['owner']['login'])
    # print('Stars：', repo_dict['stargazers_count'])
    # print("Repository：", repo_dict["html_url"])
    # print("Description：", repo_dict["description"])
# 可视化
# my_style = (base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000  # 自定义宽度，让图表更充分地利用浏览器的可用空间。

chart = pygal.Bar(my_config, style=LCS)
chart.title = "Most-Starred Python Project on GitHub"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file("python_repos.svg")
# print(stars)
# 研究第一个仓库
repo_dicts = repo_dicts[0]
print("\nKeys:", len(repo_dicts))
for key in sorted(repo_dicts.keys()):
    print(key)

# 处理结果
print(response_dict.keys())
