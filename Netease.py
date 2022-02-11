import requests
from copyheaders import headers_raw_to_dict
import json
import encrypt
import pandas as pd


class NeteaseMusic():
    def __init__(self):
        self.token = 'ec1eb9f50e4505170497d999f3d969d7'  # 用户自己添加
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
        cookie: _ga=GA1.1.1048729511.1629103325; Qs_lvt_382223=1629103325; Qs_pv_382223=459897220871502800; _ntes_nnid=cd03c58fb5fcdff26dca50bfad3dbc5e,1629103325602; _ntes_nuid=cd03c58fb5fcdff26dca50bfad3dbc5e; _clck=155jmxr|1|etx; _ga_C6TGHFPQ1H=GS1.1.1629103325.1.0.1629103332.0; vinfo_n_f_l_n3=7f460ce273df2509.1.0.1630494303935.0.1630494603171; _iuqxldmzr_=32; NMTID=00OelitiKEzgGo2a0t8iXe3XiUquxkAAAF-0l68vA; WEVNSM=1.0.0; WNMCID=spenol.1644206933788.01.0; WM_TID=4RYz%2FUdEY09AUEFUABY%2FoO1Koi2axpK9; ntes_kaola_ad=1; __remember_me=true; MUSIC_U=f189b537ee5001b24663937178cbfd79a177d1f7c981493c3f49c1294ebc1eb4519e07624a9f0053d78b6050a17a35e705925a4e6992f61dfe3f0151024f9e31; __csrf=ec1eb9f50e4505170497d999f3d969d7; WM_NIKE=9ca17ae2e6ffcda170e2e6eebbcc628b929c9ad03c81a88ea2d84f928f9eafaa25a2b8fbdace4989afafb8c82af0fea7c3b92afba6f9bbcd6a91ba85d6c76e88aea1b3d34993bdbf8de874f2b488b0c534e9adfc8ff939b691b782fc548b958ab6ee7eb48787abe55ab59db891c153b49b8b8cc221adeb8782bc3bb1f08b96f554969e8e93bb6bf8b0a7a9b23cbcb0ab9aec3cbbecaf88c76eb4f58999fc3d949aacd3fb39f5f583d2d36787a6bf8cf6738eb6aeb6f637e2a3; WM_NI=9z7ZNbSfK5DfDroRPCQcqlex2lHOF8%2Bs4nz3vOyayXIKFUovpYIJfRwCxpBYpEEkC%2Bo5Ia91s0EuvXVBBr8a4piH30xpeyi0y4agDfp%2BGxy7PFd2x37%2BM1PmEzqkwyNjbUw%3D; JSESSIONID-WYYY=HZjF8imxzuHmqaNRnONW72hs%5C0EhSi9KhkT1QkR7TT%2BTsGgkW7gmrp2gUalW%5CAXjJ%2F2%5C6QDxBhI%5CjqTNkvjeRUkdWx0dDy8o8cKQKrUwcebF8bI4fi8lW2ltd%5CU%2F5dDK0gtT5qU2gn%2F2Nohw7%5CWmcqvUONY0Ui73p2ZIyMfFn724kBnc%3A1644564917702
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
