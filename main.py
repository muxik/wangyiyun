# !/usr/bin/python3
import colorama
import os
import keyboard
from src import NetEase


colorama.init()

music = NetEase.NetEase()


def line(num):
    line = ""
    for i in range(num):
        line += "--"
    return line


while True:
    print(colorama.Fore.GREEN + '输入歌曲名开始网抑云("Ctrl+c"退出)' + colorama.Style.RESET_ALL)
    keyword = input(":")
    info = music.getMusicInfo(keyword=keyword)
    for i in range(len(info)):
        print(
            line(17)
            + "\nId: "
            + str(i)
            + "\n曲名: "
            + info[i]["name"]
            + "\n歌手: "
            + info[i]["artists"][0]["name"]
        )

    print(line(17))
    inputId = int(input("请输入Id选择歌曲:"))
    musicId = music.getMusicId(name=keyword, id=inputId)
    os.system("clear")

    print("获取网抑云评论成功！")
    comments = music.getComment(id=musicId)
    for i in range(len(comments)):
        print("+" + line(len(comments[i]["content"])) + "+")
        print(colorama.Fore.RED + comments[i]["content"] + colorama.Style.RESET_ALL)
        print("+" + line(len(comments[i]["content"])) + "+\n")
