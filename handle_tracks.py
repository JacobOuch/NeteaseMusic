import re
import pandas as pd


# 保持不变
# def get_english_ids():
#     df = pd.read_csv('唔係咁打嘅喜欢的音乐.csv',
#                      sep=',',
#                      encoding='utf-8')  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
#     del df['Unnamed: 0']  # 删除Unnamed列
#     pat_english = re.compile(r'^[A-z| |\'|\?|\&|\(|\|\.)]+$')  # 匹配全英文的模式，包括'.?&等特殊符号
#     English, english_ids = list(), list()
#     for track in df.iterrows():
#         if re.match(pat_english, track[1][1]) and re.match(pat_english, track[1][3]):
#             English.append('1')
#             english_ids.append(track[1][2])
#         else:
#             English.append(' ')
#     df["English"] = English
#     # print(df.head())
#     df.to_csv('.\changed_唔係咁打嘅喜欢的音乐.csv', sep=',', encoding='utf-8')
#     return english_ids


def get_language_ids(func):
    def inner_func():
        df = pd.read_csv('唔係咁打嘅喜欢的音乐.csv',
                         sep=',',
                         encoding='utf-8')  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
        del df['Unnamed: 0']  # 删除Unnamed列
        func(df)
        # df.to_csv('.\changed_唔係咁打嘅喜欢的音乐.csv', sep=',', encoding='utf-8')
    return inner_func


@get_language_ids
def get_english_ids(*args):
    pat_english = re.compile(r'^[A-z| |\'|\?|\&|\(|\|\.)]+$')  # 匹配全英文的模式，包括'.?&等特殊符号
    df = args[0]
    English, english_ids = list(), list()
    for track in df.iterrows():
        if re.match(pat_english, track[1][1]) and re.match(pat_english, track[1][3]):
            English.append('1')
            english_ids.append(track[1][2])
    df["English"] = English
    print(df.head())
    return english_ids


if __name__ == '__main__':
    get_english_ids()
