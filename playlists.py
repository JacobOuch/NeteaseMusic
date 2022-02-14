"""
@Author: JacobOuch
@License:
@Contact: 943411478@qq.com
@File: sort_tracks.py
@Time: 2022/2/14 下午 1:16
@Software: PyCharm
@Description: 调用程序中的所有包完成移动歌曲的操作。
"""

import sys
import sort_tracks
from Netease import NeteaseMusic

if __name__ == '__main__':
    """
    我喜欢"的歌单id：427248017
    华语：7284711237
    English：7273127486
    日语：7222794221
    韩语：7285069246
    """
    neteasemusic = NeteaseMusic()
    result = neteasemusic.get_tracks_information(playlistid='427248017')  # 根据所给的歌单id获取歌单信息
    if result:
        neteasemusic.df_to_csv(result)  # 将获取的歌单信息存入以歌单名称命名的CSV文件中
    else:
        print('获取不到歌单信息，请查看是否已经加入cookie和更新token')
        sys.exit()
    ids = sort_tracks.get_ids(result['playlist'])  # 根据存储的CSV文件获得按语言分类的字典，并同步生成一个新的CSV文件，包含语言分类信息，用于对照调试程序。
    """操作韩文歌"""
    # kr_ids = [str(id) for id in ids['korean_ids']]
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7285069246', trackids=kr_ids)    # 从我喜欢剪切韩文歌到韩语

    """操作日文歌"""
    # jp_ids = [str(id) for id in ids['japanese_ids']]
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7222794221', trackids=jp_ids)  # 从我喜欢剪切日文歌到日语
    # neteasemusic.move_songs(playlistid='7222794221', trackids=jp_ids, op='add')    # 将日文歌加到《日語》歌单
    # neteasemusic.move_songs(playlistid='427248017', trackids=jp_ids, op='del')    # 将日文歌从我喜欢中删除

    """操作英文歌"""
    en_ids = [str(id) for id in ids['english_ids']]
    neteasemusic.move_songs(playlistid='7273127486', trackids=en_ids, op='add')  # 将英文歌加到《English》歌单
    # neteasemusic.move_songs(playlistid='427248017', trackids=en_ids, op='del')    # 将英文歌从我喜欢中删除
    # neteasemusic.cut_songs(src_playlist='427248017', des_playlist='7273127486', trackids=en_ids)   # 从我喜欢剪切英文歌到english

    """操作中文歌"""
    # ch_ids = [str(id) for id in ids['chinese_ids']]
    # neteasemusic.move_songs(playlistid='7284711237', trackids=ch_ids, op='add')    # 将华语歌加到《华语》歌单
