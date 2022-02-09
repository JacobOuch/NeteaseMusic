import pandas as pd


def read_csv():
    df = pd.read_csv('唔係咁打嘅喜欢的音乐.csv', header=None,
                     sep=',', encoding='utf-8')  # filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
    print(df.head())
    print(df.tail())

if __name__ == '__main__':
    read_csv()