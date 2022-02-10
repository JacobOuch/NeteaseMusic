import requests
import js2py
from copyheaders import headers_raw_to_dict
from Crypto.Cipher import AES
import random
import codecs
import json
import base64
import pandas as pd
import handle_tracks


"""
/*
	使用
	brx0x(["流泪", "强"])                   010001
	brx0x(Xs2x.md) 						      00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
	brx0x(["爱心", "女孩", "惊恐", "大笑"])     0CoJUm6Qyw8W8jud
	这里只有 i7b 是不固定的其他都是固定的，好像
*/
var bVj8b = window.asrsea(JSON.stringify(i7b), brx0x(["流泪", "强"]), brx0x(Xs2x.md), brx0x(["爱心", "女孩", "惊恐", "大笑"]));
i7b = {
    logs: '[{"action":"bannerimpress","json":{"type":"10_专辑","url":"/album?id=86495711","id":"86495711","position":2}}]',
	csrf_token: ""
}
"""
PUB_KEY = b"010001"
MODULUS = b"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
KEY = b"0CoJUm6Qyw8W8jud"
IV = b"0102030405060708"


def get_random_str(n):
    """
    产生指定n位数的随机字符串 [a-zA-Z0-9]
    :param n: 随机字符串的位数
    :return:
    """
    text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_str = ""
    # return "".join([random_str+random.choice(text) for i in range(n)]).encode("utf-8")
    return b"abcdefghijklmnop"


def add_to_16(text):
    """
    AES 算法要求明文的字节是16的倍数
        补足为16的倍数
    :param text: 要加密的文本
    :return:
    """
    text += b"\x01" * (16 - len(text) % 16)  # 注意是 不是 \x00
    return text


def encrypt_AES(plaintext, key, iv):
    """
    AES加密
    :param plaintext: 要加密的内容都是16位的字节数据
    :param key: 密钥
    :param iv: 偏移
    :return: 二进制的密文
    """
    # 创建一个 AES 对象
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    # 加密 明文
    ciphertext = aes.encrypt(add_to_16(plaintext))
    return base64.b64encode(ciphertext)


def encrypt_RSA(plaintext, pub_key, modulus):
    """
    RSA 加密
    :param plaintext:
    :param pub_key: 公钥 010001
    :param modulus: 00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
    :return: 二进制的密文
    """
    """
    modulus =
    """
    plaintext = plaintext[::-1]
    rs = int(codecs.encode(plaintext, 'hex_codec'),
             16) ** int(pub_key, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def encrypt_WangYiYun(plaintext, pub_key=PUB_KEY, modulus=MODULUS, key=KEY):
    """
    网易云音乐加密算法
    :param plaintext: 加密的文本
    :param pub_key: RSA公钥
    :param modulus: AES
    :param key: AES密钥
    :return:
    """
    """
    /*
    * 使用d,g AES加密产生加密enctext
    * 使用e,f RSA加密产生 encSecKey
    */
    function d(d, e, f, g) {
        var h = {} // 对象
        , i = a(16); // 16位的随机字符串
        return h.encText = b(d, g), // g为秘钥对d进行加密
            h.encText = b(h.encText, i), // 又进行了一次加密，使用 i 16位的随机字符串
            h.encSecKey = c(i, e, f), // 使用rsa加密
            h // 最后返回 h 对象
    }
    """
    # 1. 产生16位的随机字符串
    random_16 = get_random_str(16)
    # 2. 获取encText
    encText = encrypt_AES(plaintext, key, IV)
    encText = encrypt_AES(encText, random_16, IV)
    # 3. 获取encSecKey
    encSecKey = encrypt_RSA(random_16, pub_key, modulus)
    return {"params": encText.decode("utf-8"), "encSecKey": encSecKey}


def df_to_csv(dictonary):
    tracks_dataframe = pd.DataFrame(dictonary)
    # tracks_dataframe = pd.DataFrame(columns=list(dictonary.keys())[1:], data=list(dictonary.values()[1:]))
    tracks_dataframe.to_csv(f".\\{dictonary['playlist']}.csv", encoding='utf-8')

    pass


class NeteaseMusic():
    def __init__(self):
        pass

    def get_needed_parameters(self, i7b):
        needed_parameters = dict()
        needed_parameters['headers'] = headers_raw_to_dict(b'''
        accept: */*
        accept-encoding: gzip, deflate, br
        accept-language: zh-CN,zh;q=0.9,en;q=0.8
        content-length: 576
        content-type: application/x-www-form-urlencoded
        cookie: _ga=GA1.1.1048729511.1629103325; Qs_lvt_382223=1629103325; Qs_pv_382223=459897220871502800; _ntes_nnid=cd03c58fb5fcdff26dca50bfad3dbc5e,1629103325602; _ntes_nuid=cd03c58fb5fcdff26dca50bfad3dbc5e; _clck=155jmxr|1|etx; _ga_C6TGHFPQ1H=GS1.1.1629103325.1.0.1629103332.0; vinfo_n_f_l_n3=7f460ce273df2509.1.0.1630494303935.0.1630494603171; _iuqxldmzr_=32; NMTID=00OelitiKEzgGo2a0t8iXe3XiUquxkAAAF-0l68vA; WEVNSM=1.0.0; WNMCID=spenol.1644206933788.01.0; WM_TID=4RYz%2FUdEY09AUEFUABY%2FoO1Koi2axpK9; WM_NI=trtJFdDrEbgS9gh4t6imeCY9%2BNJgRH2GEPuISkQzDvwAHgc4QMeu95%2BK5pRkYXA9J9wLNsrOtiVT%2B1I7fW6rvdB25DfN52gkO4GyrcNFH1E0dozwk%2BRmiWtEIu8QpVIYREo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89d87df48882d0cc3f81ef8ea3d44f969e9fafaa7b89bc82aff162f386a5d7ef2af0fea7c3b92ab8aebcabc57088ae8b83e659fbb9a8d5f73eabb3aba4dc33e9928688d144f2998bb1f84391b59f9bc77eb59f8888e2409393ab96bc3fe995fb91d1619b888fdac933b5948294f145b8b79ab5aa3b8be9aab8b57ab6bc8ed3b850a692fbd3e6618dec899af1698e9a88d2c83ca8b1b698ea2192b3a7b8f74f8babf8b2f35e8b879ea6ee37e2a3; MUSIC_U=f189b537ee5001b24663937178cbfd7995148c9f4bf89ca87ec550beffe3408e519e07624a9f0053d78b6050a17a35e705925a4e6992f61dfe3f0151024f9e31; __csrf=bc5475e560cb2023ad355da57937c2f3; ntes_kaola_ad=1; JSESSIONID-WYYY=Km%2Fy9AO%2B%2BVY9fpbTy%2F8qtnkZNpIAmnA2eMCk05rt3vKminzSfOpflJy%5CX3eznsZ%2FzuCIgK2%2Bbeoup%2FZZFf5SncsxKaquAvrAMp51YvQ28GexU1KIIZntHQ9RTn95GBrcuiQll6YhK5Tz%2Fi8gkvTQFh3nScwp2DA%2FDekh4TAYyGZ5uPZK%3A1644224619057
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
        params_and_encSecKey = encrypt_WangYiYun(plaintext=i7b)
        needed_parameters['data'] = {
            'params': params_and_encSecKey['params'],
            'encSecKey': params_and_encSecKey['encSecKey'],
        }
        return needed_parameters

    def move_songs(self, playlistid: str, trackids: list, op: str) -> dict:
        """
        :param playlistid: 被操作的歌单id
        :param trackid: 被操作的歌id
        :return: code为200则成功，502为歌曲重复
        """
        i7b = {
            'csrf_token': "bc5475e560cb2023ad355da57937c2f3",
            'op': f"{op}",  # 如果要删除对应歌单里的某首歌，可以直接把op的值改成del
            'pid': f"{playlistid}",
            'trackIds': f"{trackids}",
            'tracks': "[object Object]",
        }
        i7b = json.dumps(i7b, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        needed_parameters = self.get_needed_parameters(i7b)
        headers = needed_parameters['headers']
        data = needed_parameters['data']
        url = "https://music.163.com/weapi/playlist/manipulate/tracks?csrf_token=bc5475e560cb2023ad355da57937c2f3"
        # url = "https://music.163.com/weapi/playlist/manipulate/tracks?csrf_token=b08c761c098f97ef361342261fbf40f5"

        response = requests.post(url=url, data=data, headers=headers)
        print(response.json())
        return response.json()

    def get_tracks_information(self, playlistid: str) -> dict:
        i7b = {
            'csrf_token': "bc5475e560cb2023ad355da57937c2f3",
            'id': f"{playlistid}",
            'limit': "2000",
            'n': "2000",
            'offset': "0",
            'total': "true"
        }
        i7b = json.dumps(i7b, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        needed_parameters = self.get_needed_parameters(i7b)
        headers = needed_parameters['headers']
        data = needed_parameters['data']
        url = "https://music.163.com/weapi/v6/playlist/detail"
        response = requests.post(url=url, data=data, headers=headers)
        response_json = response.json()
        # response_json = json.dumps(response.json(), ensure_ascii=False)
        playlist = response_json['playlist']['name']
        names = [track['name'] for track in response_json['playlist']['tracks']]
        trackids = [track['id'] for track in response_json['playlist']['tracks']]
        singers = [track['ar'][0]['name'] for track in response_json['playlist']['tracks']]
        singerids = [track['ar'][0]['id'] for track in response_json['playlist']['tracks']]
        albums = [track['al']['name'] for track in response_json['playlist']['tracks']]
        tracks_information = {'playlist': playlist, 'names': names, 'ids': trackids, 'singers': singers,
                              'singerids': singerids, 'albums': albums}
        return tracks_information

    def cut_songs(self, **kwargs):
        self.move_songs(playlistid=kwargs['des_playlist'], trackids=kwargs['trackids'], op='add')   # 先添加到目的歌单
        self.move_songs(playlistid=kwargs['src_playlist'], trackids=kwargs['trackids'], op='del')   # 再从源歌单删除


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
    df_to_csv(result)
    ids = handle_tracks.get_ids()
    kr_ids = [str(id) for id in ids['korean_ids']]
    jp_ids = [str(id) for id in ids['japanese_ids']]
    en_ids = [str(id) for id in ids['english_ids']]
    ch_ids = [str(id) for id in ids['chinese_ids']]
    # neteasemusic.move_songs(playlistid='7222794221', trackids=jp_ids, op='add')    # 将日文歌加到《日語》歌单
    # neteasemusic.move_songs(playlistid='7273127486', trackids=en_ids, op='add')    # 将英文歌加到《English》歌单
    # neteasemusic.move_songs(playlistid='7284711237', trackids=ch_ids, op='add')    # 将华语歌加到《华语》歌单
    # neteasemusic.move_songs(playlistid='427248017', trackids=en_ids, op='del')    # 将英文歌从我喜欢中删除
    # neteasemusic.move_songs(playlistid='427248017', trackids=jp_ids, op='del')    # 将日文歌从我喜欢中删除
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7273127486', trackids=en_ids)    # 从我喜欢剪切英文歌到english
    neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7222794221', trackids=jp_ids)    # 从我喜欢剪切日文歌到日语
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7285069246', trackids=kr_ids)    # 从我喜欢剪切韩文歌到韩语
