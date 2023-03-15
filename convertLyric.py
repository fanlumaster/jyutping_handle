'''
将粤语的歌词加上粤拼(jp)之后输出到 res_lyric.txt 文件中
'''

import os.path

file_path = os.path.join(os.path.dirname(__file__), './res/jp.txt')

my_dict = {}
with open(file_path, 'rb+') as myfile:
    contents = myfile.readlines()
    for line in contents:
        cur_pair = line.decode().split('\t')
        if cur_pair[0] in my_dict.keys():
            continue
        my_dict[cur_pair[0]] = cur_pair[1]

lyrics_path = os.path.join(os.path.dirname(__file__), 'lyric.txt')
my_lyrics = ''''''
with open(lyrics_path, 'rb+') as f:
    my_lyrics = f.read().decode()

res_lyrics = ''


def is_chinese(ch):
    if '\u4300' <= ch <= '\u9fff':
        return True
    return False


# 从魔镜歌词网上复制下来的歌词有时候会有它这个广告插在其中，我们需要将其去掉
my_lyrics = my_lyrics.replace('更多更详尽歌词 在 ※ Mojim.com　魔镜歌词网\n', '')

for i in range(len(my_lyrics)):
    cur_char = my_lyrics[i]
    if (is_chinese(cur_char)):
        cur_res = cur_char + '(' + my_dict[cur_char][:-1] + ')'
        res_lyrics += cur_res
    else:
        res_lyrics += cur_char

res_lyric_path = os.path.join(os.path.dirname(__file__), 'res_lyric.txt')
with open(res_lyric_path, 'wb+') as f:
    f.write(res_lyrics.encode())
