# !/usr/bin/python3

import os
from src import NetEase

music = NetEase.NetEase()

while True:

    keyword = input("输入歌曲名开始网抑云:")
    info = music.getMusicInfo(keyword=keyword)
    for i in range(len(info)):
        print(
            "--------------------------------"
            + "\nId: "
            + str(i)
            + "\n曲名: "
            + info[i]["name"]
            + "\n歌手: "
            + info[i]["artists"][0]["name"]
        )

    print("--------------------------------")
    inputId = int(input("请输入Id选择歌曲:"))
    musicId = music.getMusicId(name=keyword, id=inputId)
    os.system("clear")
    print("获取网抑云评论成功！")
    comments = music.getComment(id=musicId)
    for i in range(len(comments)):
        print("+ - - - - - - - - - - - - - - +")
        print(comments[i]["content"] + "\n")
