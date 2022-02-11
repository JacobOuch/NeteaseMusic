import re
import pandas as pd


def get_ids(playlist):
    """
        返回歌曲id字典，字典按歌曲语言进行分类，函数中的language（小写）用来存储对应歌曲的语言，并将对应语言保存在CSV文件中
    :return: ids字典，其中 english_ids存放英文歌的列表，chinese_ids存放中文歌的列表，japanese_ids存放日文歌的列表
    """
    # 匹配全英文的模式，包括',.?&|()!-/等特殊符号
    # en_pattern = re.compile(r'^[A-z| |0-9|\'|\,|\.|\?|\&|\||\(|\)|\!|\-|\/|\*|\@|\$|\%|\~]+$')
    en_pattern = re.compile(r'^[\x20-\x7e]+$')  # 匹配全英文的模式，包括特殊符号
    ch_pattern = re.compile(r'[\u4E00-\u9FA5|\u4E00-\u9FFF]+')  # 匹配中文
    jp_pattern = re.compile(r'[\u3040-\u309f|\u30a0-\u30ff]+')  # 匹配日文
    kr_pattern = re.compile(r'[\uac00-\ud7ff]+')  # 匹配韩文
    df = pd.read_csv(f'{playlist}.csv', sep=',',  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，
                     encoding='utf-8')  # sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。

    del df['Unnamed: 0']  # 删除Unnamed列
    language, ids = list(), dict()
    ids['english_ids'], ids['chinese_ids'], ids['japanese_ids'], ids['korean_ids'] = [], [], [], []
    for track in df.iterrows():  # 详看iterrows函数的解释，0对应的是索引，1对应的是行的数据
        if re.match(en_pattern, track[1]['names']) and re.match(en_pattern, track[1]['singers']):
            # 用match是因为大部分英文歌曲的歌手名和歌曲名都应该匹配英文模式，但有可能存在bug，无法匹配中文的’，但是在单独测试是可以匹配的，但这个程序中无法匹配，找不出原因
            language.append('en')
            ids['english_ids'].append(track[1]['ids'])
        # 日语优先级比中文高，因为日语中可能有简体中文，中日韩文均是可以用search来匹配，只要搜到对应的文字就可以当成是该种语言的歌曲
        elif re.search(jp_pattern, track[1]['names']) or re.search(jp_pattern, track[1]['singers']):
            language.append('jp')
            ids['japanese_ids'].append(track[1]['ids'])
        elif re.search(ch_pattern, track[1]['names']) or re.search(ch_pattern, track[1]['singers']):
            language.append('ch')
            ids['chinese_ids'].append(track[1]['ids'])
        elif re.search(kr_pattern, track[1]['names']) or re.search(kr_pattern, track[1]['singers']):
            language.append('kr')
            ids['korean_ids'].append(track[1]['ids'])
        else:
            language.append('unknown')

    df['Language'] = language  # 新增一列保存歌曲的语言
    # print(df.head(7))
    df.to_csv(f'.\changed_{playlist}.csv', sep=',', encoding='utf-8')
    return ids


# 以下为装饰器的尝试，未完善
# def get_language_ids(func):
#     def inner_func():
#         df = pd.read_csv('唔係咁打嘅喜欢的音乐.csv',
#                          sep=',',
#                          encoding='utf-8')  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
#         del df['Unnamed: 0']  # 删除Unnamed列
#         func(df)
#         # df.to_csv('.\changed_唔係咁打嘅喜欢的音乐.csv', sep=',', encoding='utf-8')
#     return inner_func
#
#
# @get_language_ids
# def get_english_ids(*args):
#     pat_english = re.compile(r'^[A-z| |\'|\?|\&|\(|\|\.)]+$')  # 匹配全英文的模式，包括'.?&等特殊符号
#     df = args[0]
#     English, english_ids = list(), list()
#     for track in df.iterrows():
#         if re.match(pat_english, track[1][1]) and re.match(pat_english, track[1][3]):
#             English.append('1')
#             english_ids.append(track[1][2])
#     df["English"] = English
#     print(df.head())
#     return english_ids


if __name__ == '__main__':
    get_ids()
