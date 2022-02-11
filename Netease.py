import requests
from copyheaders import headers_raw_to_dict
import json
import encrypt
import pandas as pd


class NeteaseMusic():
    def __init__(self):
        self.token = '自己添加'  # 用户自己添加
        pass

    def encrypt_parameters(self, i7b):
        """
        利用加密文件加密要向服务器传送的数据
        :param i7b: 需要向服务器传送的数据，str类型
        :return:
        """
        needed_parameters = dict()
        """        
            需要在以下的headers文件中加入cookie才可以正常运行，否则服务器会提示“需要登录”
        """
        needed_parameters['headers'] = headers_raw_to_dict(b'''
        accept: */*
        accept-encoding: gzip, deflate, br
        accept-language: zh-CN,zh;q=0.9,en;q=0.8
        content-length: 576
        content-type: application/x-www-form-urlencoded
        nm-gcore-status: 1
        cookie: 自己添加
        origin: https://music.163.com
        referer: https://music.163.com/my/
        sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"
        sec-ch-ua-mobile: ?0
        sec-ch-ua-platform: "Windows"
        sec-fetch-dest: empty
        sec-fetch-mode: cors
        sec-fetch-site: same-origin
        user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36
        ''')
        params_and_encSecKey = encrypt.encrypt_WangYiYun(plaintext=i7b)
        needed_parameters['data'] = {
            'params': params_and_encSecKey['params'],
            'encSecKey': params_and_encSecKey['encSecKey'],
        }
        return needed_parameters

    def move_songs(self, playlistid: str, trackids: list, op: str) -> dict:
        """
            操作传入的歌单和歌曲，根据参数op决定是添加歌曲还是删除歌曲，
            比如要像歌单123中加入为歌曲id为456，789的歌，playlistid就为123，trackids就是[456,789]，op是'add'
        :param playlistid:对象歌单
        :param trackids:对象歌曲，列表
        :param op: operation，可以为add或者del
        :return:
        """
        i7b = {
            'csrf_token': self.token,
            'op': f"{op}",  # 如果要删除对应歌单里的某首歌，可以直接把op的值改成del
            'pid': f"{playlistid}",
            'trackIds': f"{trackids}",
            'tracks': "[object Object]",
        }
        i7b = json.dumps(i7b, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        needed_parameters = self.encrypt_parameters(i7b)
        headers = needed_parameters['headers']
        data = needed_parameters['data']
        url = f"https://music.163.com/weapi/playlist/manipulate/tracks?csrf_token={self.token}"
        response = requests.post(url=url, data=data, headers=headers)
        # json中code为200则成功，502为歌曲重复
        print(response.json())

    def get_tracks_information(self, playlistid: str) -> dict:
        """
        根据传入的歌单id参数获取歌单的信息，信息包括歌单名字、歌曲名、歌曲id、歌手名、歌手id、专辑名
        :param playlistid: 传入的歌单id参数
        :return: 返回一个包含歌单中前1000首歌曲信息的字典
        """
        tracks_information = dict()
        i7b = {
            'csrf_token': f"{self.token}",
            'id': f"{playlistid}",
            'limit': "2000",
            'n': "2000",
            'offset': "0",
            'total': "true"
        }
        i7b = json.dumps(i7b, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        needed_parameters = self.encrypt_parameters(i7b)
        headers = needed_parameters['headers']
        data = needed_parameters['data']
        url = "https://music.163.com/weapi/v6/playlist/detail"
        response = requests.post(url=url, data=data, headers=headers)
        response_json = response.json()
        if response_json['code'] == 200:
            try:
                playlist = response_json['playlist']['name']
                names = [track['name'] for track in response_json['playlist']['tracks']]
                trackids = [track['id'] for track in response_json['playlist']['tracks']]
                singers = [track['ar'][0]['name'] for track in response_json['playlist']['tracks']]
                singerids = [track['ar'][0]['id'] for track in response_json['playlist']['tracks']]
                albums = [track['al']['name'] for track in response_json['playlist']['tracks']]
                tracks_information = {'playlist': playlist, 'names': names, 'ids': trackids, 'singers': singers,
                                      'singerids': singerids, 'albums': albums}
            except Exception as e:
                print(e)
        else:
            print(response_json['code'], response_json['message'])
        return tracks_information

    def cut_songs(self, **kwargs):
        """
        调用move_songs函数实现歌曲的剪切功能
        :param kwargs: des_playlist表示目的歌单，src_playlist表示源歌单
        :return:
        """
        self.move_songs(playlistid=kwargs['des_playlist'], trackids=kwargs['trackids'], op='add')  # 先添加到目的歌单
        self.move_songs(playlistid=kwargs['src_playlist'], trackids=kwargs['trackids'], op='del')  # 再从源歌单删除

    def df_to_csv(self, dictonary):
        """
        将传入的字典用csv存储，以歌单的名称命名
        :return:
        """
        tracks_dataframe = pd.DataFrame(dictonary)
        tracks_dataframe.to_csv(f".\\{dictonary['playlist']}.csv", encoding='utf-8')
