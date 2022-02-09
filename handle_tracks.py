import pandas as pd


def read_csv():
    df = pd.read_csv('唔係咁打嘅喜欢的音乐.csv', header=0,
                     sep=',',
                     encoding='utf-8')  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
    English = list()
    print(df.head())
    for track in df.iterrows():
        if track[1][2].startswith('C'):
            English.append('1')
        else:
            English.append('2')
    df["English"] = English
    print(df.head())

if __name__ == '__main__':
    read_csv()
