import re

st = '호랑수월가'
if re.search(r'[\uac00-\ud7ff]+', st):
    print('1')