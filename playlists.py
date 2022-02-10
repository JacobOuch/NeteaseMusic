import requests
from copyheaders import headers_raw_to_dict
import random
import json
import pandas as pd
import handle_tracks
import encrypt


class NeteaseMusic():
    def __init__(self):
        self.token = 'bc5475e560cb2023ad355da57937c2f3'
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
            cookie: _ga=GA1.1.1048729511.1629103325; Qs_lvt_382223=1629103325; Qs_pv_382223=459897220871502800; _ntes_nnid=cd03c58fb5fcdff26dca50bfad3dbc5e,1629103325602; _ntes_nuid=cd03c58fb5fcdff26dca50bfad3dbc5e; _clck=155jmxr|1|etx; _ga_C6TGHFPQ1H=GS1.1.1629103325.1.0.1629103332.0; vinfo_n_f_l_n3=7f460ce273df2509.1.0.1630494303935.0.1630494603171; _iuqxldmzr_=32; NMTID=00OelitiKEzgGo2a0t8iXe3XiUquxkAAAF-0l68vA; WEVNSM=1.0.0; WNMCID=spenol.1644206933788.01.0; WM_TID=4RYz%2FUdEY09AUEFUABY%2FoO1Koi2axpK9; WM_NI=trtJFdDrEbgS9gh4t6imeCY9%2BNJgRH2GEPuISkQzDvwAHgc4QMeu95%2BK5pRkYXA9J9wLNsrOtiVT%2B1I7fW6rvdB25DfN52gkO4GyrcNFH1E0dozwk%2BRmiWtEIu8QpVIYREo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89d87df48882d0cc3f81ef8ea3d44f969e9fafaa7b89bc82aff162f386a5d7ef2af0fea7c3b92ab8aebcabc57088ae8b83e659fbb9a8d5f73eabb3aba4dc33e9928688d144f2998bb1f84391b59f9bc77eb59f8888e2409393ab96bc3fe995fb91d1619b888fdac933b5948294f145b8b79ab5aa3b8be9aab8b57ab6bc8ed3b850a692fbd3e6618dec899af1698e9a88d2c83ca8b1b698ea2192b3a7b8f74f8babf8b2f35e8b879ea6ee37e2a3; MUSIC_U=f189b537ee5001b24663937178cbfd7995148c9f4bf89ca87ec550beffe3408e519e07624a9f0053d78b6050a17a35e705925a4e6992f61dfe3f0151024f9e31; __csrf=bc5475e560cb2023ad355da57937c2f3; ntes_kaola_ad=1; JSESSIONID-WYYY=Km%2Fy9AO%2B%2BVY9fpbTy%2F8qtnkZNpIAmnA2eMCk05rt3vKminzSfOpflJy%5CX3eznsZ%2FzuCIgK2%2Bbeoup%2FZZFf5SncsxKaquAvrAMp51YvQ28GexU1KIIZntHQ9RTn95GBrcuiQll6YhK5Tz%2Fi8gkvTQFh3nScwp2DA%2FDekh4TAYyGZ5uPZK%3A1644224619057
        """
        needed_parameters['headers'] = headers_raw_to_dict(b'''
        accept: */*
        accept-encoding: gzip, deflate, br
        accept-language: zh-CN,zh;q=0.9,en;q=0.8
        content-length: 576
        content-type: application/x-www-form-urlencoded
        nm-gcore-status: 1
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

    def df_to_csv(dictonary):
        """
        将传入的字典用csv存储，以歌单的名称命名
        :return:
        """
        tracks_dataframe = pd.DataFrame(dictonary)
        tracks_dataframe.to_csv(f".\\{dictonary['playlist']}.csv", encoding='utf-8')


if __name__ == '__main__':
    """
    我喜欢"的歌单id：427248017
    华语：7284711237
    English：7273127486
    日语：7222794221
    韩语：7285069246
    """
    neteasemusic = NeteaseMusic()
    result = neteasemusic.get_tracks_information(playlistid='427248017')
    if result:
        neteasemusic.df_to_csv(result)
    else:
        print('获取不到歌单信息，请查看是否已经加入cookies和更新token')
    ids = handle_tracks.get_ids(result['playlist'])
    # kr_ids = [str(id) for id in ids['korean_ids']]
    # jp_ids = [str(id) for id in ids['japanese_ids']]
    # en_ids = [str(id) for id in ids['english_ids']]
    # ch_ids = [str(id) for id in ids['chinese_ids']]
    # neteasemusic.move_songs(playlistid='7222794221', trackids=jp_ids, op='add')    # 将日文歌加到《日語》歌单
    # neteasemusic.move_songs(playlistid='7273127486', trackids=en_ids, op='add')    # 将英文歌加到《English》歌单
    # neteasemusic.move_songs(playlistid='7284711237', trackids=ch_ids, op='add')    # 将华语歌加到《华语》歌单
    # neteasemusic.move_songs(playlistid='427248017', trackids=en_ids, op='del')    # 将英文歌从我喜欢中删除
    # neteasemusic.move_songs(playlistid='427248017', trackids=jp_ids, op='del')    # 将日文歌从我喜欢中删除
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7273127486', trackids=en_ids)   # 从我喜欢剪切英文歌到english
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7222794221', trackids=jp_ids)  # 从我喜欢剪切日文歌到日语
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7285069246', trackids=kr_ids)    # 从我喜欢剪切韩文歌到韩语
