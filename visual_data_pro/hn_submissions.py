#!/usr/bin/python3
# coding : utf-8
# @Time  : 2020/11/24 19:29
# @File  : hn_submissions.py
__author__ = 'yangyanqin'

import requests
from operator import itemgetter

# 执行API调用并存储响应
url = "https://hacker-news.firebaseio.cm/v0/topstories.json"
r = requests.get(url)
print("Status Code:", r.status_code)

# 处理有关每篇文章的信息
submisssion_ids = r.json()
submisssion_dicts = []
for submisssion_id in submisssion_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submisssion_id) + ".json")
    submisssion_r = requests.get(url)
    print(submisssion_r.status_code)
    response_dict = submisssion_r.json()

    submisssion_dict = {
        "title": response_dict['title'],
        "link": 'http://news.ycombinator.com/item?id=' + str(submisssion_id),
        "comments": response_dict.get("descendants", 0)  # 不确定某个键是否包含在字典中时，
        # 可以使用dict.get()，它在指定的键存在时返回与之相关联的值，并在指定的键不存在时返回你指定的值（0），
    }

    submisssion_dicts.append(submisssion_dict)

    submisssion_dicts = sorted(submisssion_dicts, key=itemgetter('comments'), reverse=True)  # 根据某个值排序

    for submisssion_dict in submisssion_dicts:
        print("\nTitle:", submisssion_dict["title"])
        print("Discussion:", submisssion_dict["link"])
        print("Comments:", submisssion_dict["comments"])
