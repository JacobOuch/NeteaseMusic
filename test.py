import re

song = 'You‘re Not Alone'
singer = 'Owl City'
en_pattern = re.compile(r'[\x20-\x7e]+')
if re.match(en_pattern, song) and re.match(en_pattern, singer):
    # 用match是因为大部分英文歌曲的歌手名和歌曲名都应该匹配英文模式
    print('1')
if re.match(en_pattern, 'You’re Not Alone'):
    print(2)