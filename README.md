# NeteaseMusic

要做一个可以自动将歌单中的歌曲转移到指定歌单的python程序


以Everybody hates me为例：
分享歌曲链接为：https://music.163.com/song?id=544247523&userid=307853190

歌曲ID为544247523
对应用户的userid为307853190


可以先把A歌单中的歌曲移到B歌单，再选择性地把这首歌从A歌单中删除。

添加成功之后的response：
{
  "trackIds": "[544247523]",
  "code": 200,
  "count": 5,
  "cloudCount": 0
}