# !/usr/bin/python3

import requests
import json


class NetEase:

    url = "http://musicapi.leanapp.cn"

    def __init__(self):
        print("+ 生而为人，我很抱歉 + \n")

    def getComment(self, id):
        r = requests.get(self.url + "/comment/music?limit=10&id=" + str(id))
        data = json.loads(r.text)
        return data["hotComments"]

    def getMusicInfo(self, keyword):
        r = requests.get(self.url + "/search?limit=10&keywords=" + keyword)
        result = json.loads(r.text)
        if result["code"] != 200:
            return "歌曲不存在"
        songs = result["result"]["songs"]
        return songs

    def getMusicId(self, name, id):
        MusicId = self.getMusicInfo(name)
        return MusicId[id]["id"]
